from api.errors.ApiError import ApiError


class NoNovaResponseError(ApiError):
    def __init__(self, message="There was no NOVA response."):
        super().__init__(message)

    def log_error(self):
        self.logger.warning(self.message)
