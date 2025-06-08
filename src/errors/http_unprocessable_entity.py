class HttpUnprocessableEntity(Exception):
    def __init__(self, message: str) -> None:
        self.value = message
        self.name = "HttpUnprocessableEntity"
        self.status_code = 422

        super().__init__(self.value)