# coding: utf-8

"""
    Kimai 2 - API Docs

    JSON API for the Kimai 2 time-tracking software. Read more about its usage in the [API documentation](https://www.kimai.org/documentation/rest-api.html) and then download a [Swagger file](doc.json) for import e.g. in Postman. Be aware: it is not yet considered stable and BC breaks might happen, but we try to avoid them.   # noqa: E501

    OpenAPI spec version: 0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kimai_client
from kimai_client.models.timesheet_meta import TimesheetMeta  # noqa: E501
from kimai_client.rest import ApiException


class TestTimesheetMeta(unittest.TestCase):
    """TimesheetMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimesheetMeta(self):
        """Test TimesheetMeta"""
        # FIXME: construct object with mandatory attributes with example values
        # model = kimai_client.models.timesheet_meta.TimesheetMeta()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
