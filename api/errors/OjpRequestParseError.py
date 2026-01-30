from api.errors.ApiError import ApiError


class OjpRequestParseError(ApiError):
    def __init__(self, cause: Exception = None, message="Failed to parse OJP request."):
        self.cause = cause
        super().__init__(message, 400)

    def log_error(self):
        self.logger.warning(self.message + ": " + str(self.cause))
