from api.errors.ApiError import ApiError

class NoNovaResponseError(ApiError):
    def __init__(self, message="There was no NOVA response."):
        self.message = message
        super().__init__(self.message)

    def log_error(self):
        self.logger.warning(self.message)