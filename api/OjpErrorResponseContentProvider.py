from api.ErrorResponseContentProvider import ErrorResponseContentProvider

class OjpErrorResponseContentProvider(ErrorResponseContentProvider):

    def __init__(self):
        pass

    def provide_error_response_content(self, message: str) -> str:
        return message