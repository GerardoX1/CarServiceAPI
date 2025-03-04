from typing import Optional

from infra.mongo import MongoRepository


class DataBase:
    repository: Optional[MongoRepository] = None


db = DataBase()


async def get_repository():
    repository = db.repository
    return repository


async def open_connection():
    db.repository = MongoRepository()


async def close_connection():
    if db.repository is not None:
        db.repository.close()
