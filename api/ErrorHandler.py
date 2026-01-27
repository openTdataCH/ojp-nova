import logging

from fastapi import Response

from api.ErrorResponseContentProvider import ErrorResponseContentProvider
from api.errors import ApiError

class ErrorHandler:

    def __init__(self, response_provider: ErrorResponseContentProvider):
        self.response_provider = response_provider
        self.logger = logging.getLogger(__name__)

    def handle_error(self, error: ApiError) -> Response:
        error.log_error()
        return Response(
            self.response_provider.provide_error_response_content(error.message),
            status_code=error.status_code,
            media_type="application/xml; charset=utf-8",
        )


