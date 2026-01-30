import logging
from abc import abstractmethod, ABC

class ApiError(Exception, ABC):
    def __init__(self, message="An unspecific error occurred.", status_code=500):
        self.message = message
        self.status_code = status_code
        self.logger = logging.getLogger(__name__)
        super().__init__(self.message)

    @abstractmethod
    def log_error(self):
        self.logger.warning(self.message)
