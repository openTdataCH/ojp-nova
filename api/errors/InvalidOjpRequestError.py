from api.errors.ApiError import ApiError


class InvalidOjpRequestError(ApiError):
    def __init__(self, message="There was no (valid) OJP request."):
        super().__init__(message, 400)

    def log_error(self):
        self.logger.warning(self.message)
