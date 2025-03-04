from infra.mongo import MongoRepository

class Flow:
    def __init__(self, repository: MongoRepository):
        self._repository = repository