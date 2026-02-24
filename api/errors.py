import logging
import unittest
from abc import ABC, abstractmethod

from fastapi import Response


class ApiError(Exception, ABC):
    def __init__(self, message="An unspecific error occurred.", status_code=500):
        self.message = message
        self.status_code = status_code
        self.logger = logging.getLogger(__name__)
        super().__init__(self.message)

    @abstractmethod
    def log_error(self):
        self.logger.warning(self.message)

    def get_message(self):
        return self.message

    def get_status_code(self):
        return self.status_code


class ErrorResponseContentProvider(ABC):
    @abstractmethod
    def provide_error_response_content(self, message: str) -> str:
        """
        Provides the error response content for the given error message.
        """
        return message


class ErrorHandler:
    def __init__(self, response_provider: ErrorResponseContentProvider):
        self.response_provider = response_provider
        self.logger = logging.getLogger(__name__)

    def handle_error(self, error: ApiError) -> Response:
        """
        Handles an ApiError and creates an according Response using a ErrorResponseContentProvider.
        """
        error.log_error()
        return Response(
            self.response_provider.provide_error_response_content(error.get_message()),
            status_code=error.get_status_code(),
            media_type="application/xml; charset=utf-8",
        )


class InternalServerError(ApiError):
    def __init__(self, message="An internal server error occurred."):
        super().__init__(message)

    def log_error(self):
        self.logger.error(self.message)


class InvalidNovaResponseError(ApiError):
    def __init__(self, message="There was no valid NOVA response."):
        super().__init__(message, 400)

    def log_error(self):
        self.logger.warning(self.message)


class InvalidOjpRequestError(ApiError):
    def __init__(self, message="There was no (valid) OJP request."):
        super().__init__(message, 400)

    def log_error(self):
        self.logger.warning(self.message)


class NoNovaResponseError(ApiError):
    def __init__(self, message="There was no NOVA response."):
        super().__init__(message)

    def log_error(self):
        self.logger.warning(self.message)


class OjpRequestParseError(ApiError):
    def __init__(self, cause: Exception = None, message="Failed to parse OJP request."):
        self.cause = cause
        super().__init__(message, 400)

    def log_error(self):
        self.logger.warning(self.message + ": " + str(self.cause))


class MessageErrorResponseContentProvider(ErrorResponseContentProvider):
    def provide_error_response_content(self, message: str) -> str:
        return message


class ErrorHandlerTest(unittest.TestCase):
    logger = logging.getLogger(__name__)

    def test_ojp1_WHEN_internal_server_error_EXPECT_error_response(self):
        self._catch_internal_server_error(MessageErrorResponseContentProvider())

    def test_ojp2_WHEN_internal_server_EXPECT_error_response(self):
        self._catch_internal_server_error(MessageErrorResponseContentProvider())

    def test_ojp1_WHEN_api_error_EXPECT_error_response(self):
        self._catch_api_error(MessageErrorResponseContentProvider())

    def _catch_internal_server_error(
        self, error_response_provider: ErrorResponseContentProvider
    ):
        # prepare test case
        error_handler = ErrorHandler(error_response_provider)
        self.assertIsNotNone(error_handler)
        message = "Oups, terrible failure ;-)"
        try:
            raise InternalServerError(message)

        # run test case
        except InternalServerError as e:
            self.logger.info("caught InternalServerError ...")
            response = error_handler.handle_error(e)

            # assert expectations
            self.assertIsNotNone(response)

    def _catch_api_error(self, error_response_provider: ErrorResponseContentProvider):
        # prepare test case
        error_handler = ErrorHandler(error_response_provider)
        self.assertIsNotNone(error_handler)
        message = "Oups, terrible failure ;-)"
        try:
            raise InternalServerError(message)

        # run test case
        except ApiError as e:
            self.logger.info("caught ApiError ...")
            response = error_handler.handle_error(e)

            # assert expectations
            self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
