from api.errors.ApiError import ApiError

class InvalidOjpRequestError(ApiError):
    def __init__(self, message="There was no (valid) OJP request."):
        self.message = message
        self.status_code = 400
        super().__init__(self.message)

    def log_error(self):
        self.logger.warning(self.message)