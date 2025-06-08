class HttpBadRequest(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(self.message)
        self.message = message
        self.name = "HttpBadRequest"
        self.status_code = 400