from abc import abstractmethod, ABC


class ErrorResponseContentProvider(ABC):
    @abstractmethod
    def provide_error_response_content(self, message: str) -> str:
        """
        Provides the error response content for the given error message.
        """
        return message
