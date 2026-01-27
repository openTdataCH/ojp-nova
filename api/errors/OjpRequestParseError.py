from api.errors.ApiError import ApiError

class OjpRequestParseError(ApiError):
    def __init__(self, cause: Exception = None, message="Failed to parse OJP request."):
        self.message = message
        self.status_code = 400
        self.cause = cause
        super().__init__(self.message)

    def log_error(self):
        self.logger.warning(self.message + ": "+ str(self.cause))