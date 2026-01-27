from api.errors.ApiError import ApiError

class InternalServerError(ApiError):
    def __init__(self, message="An internal server error occurred."):
        self.message = message
        self.status_code = 500
        super().__init__(self.message)

    def log_error(self):
        self.logger.error(self.message)
