from presentation.error import BaseError, ErrorLocationEnum, Status


class InvalidBody(BaseError):
    code: str = "UNPROCESSABLE_CONTENT"
    message: str = "Invalid JSON format in request body."
    http_status = Status.UNPROCESSABLE_CONTENT

    def __init__(self):
        super().__init__(
            details="The provided request body is missing or invalid.",
            location=ErrorLocationEnum.BODY,
            displayable_message="El Body de  la solicitud proporcionado está "
            "ausente o es inválido.",
        )
