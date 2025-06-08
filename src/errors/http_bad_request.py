class HttpBadRequest(Exception):
    def __init__(self, message: str) -> None:
        self.value = message
        self.name = "HttpBadRequest"
        self.status_code = 400
        
        super().__init__(self.value)