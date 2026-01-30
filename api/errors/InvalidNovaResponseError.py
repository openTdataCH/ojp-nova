from api.errors.ApiError import ApiError


class InvalidNovaResponseError(ApiError):
    def __init__(self, message="There was no valid NOVA response."):
        super().__init__(message,400)

    def log_error(self):
        self.logger.warning(self.message)
