import sys
import traceback
from functools import wraps

from fastapi import Request, Response
from presentation.error import BaseError, DefaultError
from presentation.helpers import add_errors_to_response, destructuring
from presentation.logger import Logger
from presentation.response import Response as APIResponse
from presentation.schemas.error import ErrorLocationEnum
from presentation.status import Status
from pydantic import ValidationError


def exception_handler(
    response_status: Status = Status.OK,
    pydantic_error_location: ErrorLocationEnum = ErrorLocationEnum.BODY,
):
    def wrapper(func):
        @wraps(func)
        async def wrapped_func(request: Request, response: Response, *args, **kwargs):
            logger: Logger = Logger()
            api_response = APIResponse(logger)
            request.state.pydantic_error_location = pydantic_error_location

            try:
                api_response.status = response_status
                api_response.update_data(await func(request, response, *args, **kwargs))

            except BaseError as error:
                api_response.status = error.http_status
                api_response.add_error(error)

            except ValidationError as error:
                api_response.status = Status.BAD_REQUEST
                all_errors = destructuring(error.errors())
                add_errors_to_response(
                    api_response, all_errors, pydantic_error_location
                )

            except Exception as e:
                _, _, tb = sys.exc_info()
                logger.log_error(f"Unexpected Error! {type(e)} {str(e)}")
                logger.log_error(f"Traceback: {traceback.format_tb(tb)}")
                api_response.status = Status.INTERNAL_SERVER_ERROR
                api_response.add_error(DefaultError())

            response.status_code = api_response.code
            return api_response.response

        return wrapped_func

    return wrapper
