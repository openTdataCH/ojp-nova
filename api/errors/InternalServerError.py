from api.errors.ApiError import ApiError


class InternalServerError(ApiError):
    def __init__(self, message="An internal server error occurred."):
        super().__init__(message)

    def log_error(self):
        self.logger.error(self.message)
