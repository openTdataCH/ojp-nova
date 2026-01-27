from abc import abstractmethod, ABC

class ErrorResponseContentProvider(ABC):
    @abstractmethod
    def provide_error_response_content(self, message: str) -> str:
        return message