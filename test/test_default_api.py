# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen.   # noqa: E501

    OpenAPI spec version: 0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kimai_python
from kimai_python.api.default_api import DefaultApi  # noqa: E501
from kimai_python.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = kimai_python.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_config_i18n_get(self):
        """Test case for api_config_i18n_get

        Returns the user specific locale configuration  # noqa: E501
        """
        pass

    def test_api_config_timesheet_get(self):
        """Test case for api_config_timesheet_get

        Returns the instance specific timesheet configuration  # noqa: E501
        """
        pass

    def test_api_ping_get(self):
        """Test case for api_ping_get

        A testing route for the API  # noqa: E501
        """
        pass

    def test_api_version_get(self):
        """Test case for api_version_get

        Returns information about the Kimai release  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
