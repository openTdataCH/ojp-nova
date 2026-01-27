from api.errors.ApiError import ApiError

class InvalidNovaResponseError(ApiError):
    def __init__(self, message="There was no valid NOVA response."):
        self.message = message
        super().__init__(self.message)

    def log_error(self):
        self.logger.warning(self.message)