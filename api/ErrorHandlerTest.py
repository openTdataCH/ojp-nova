import logging
import unittest

from api.ErrorHandler import ErrorHandler
from api.ErrorResponseProvider import ErrorResponseProvider
from api.errors.ApiError import ApiError
from api.errors.InternalServerError import InternalServerError
from api.ojp1.ErrorResponseProviderOjp1 import ErrorResponseProviderOjp1
from api.ojp2.ErrorResponseProviderOjp2 import ErrorResponseProviderOjp2

class ErrorHandlerTest(unittest.TestCase):

    logger = logging.getLogger(__name__)

    def test_ojp1_WHEN_internal_server_error_EXPECT_error_response(self):
        self._catch_internal_server_error(ErrorResponseProviderOjp1())

    def test_ojp2_WHEN_internal_server_EXPECT_error_response(self):
        self._catch_internal_server_error(ErrorResponseProviderOjp2())

    def test_ojp1_WHEN_api_error_EXPECT_error_response(self):
        self._catch_api_error(ErrorResponseProviderOjp1())

    def _catch_internal_server_error(self, error_response_provider: ErrorResponseProvider):

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

    def _catch_api_error(self, error_response_provider: ErrorResponseProvider):

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

if __name__ == '__main__':
    unittest.main()