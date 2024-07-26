# coding: utf-8

"""
    Apache Iceberg REST Catalog API

    Defines the specification for the first version of the REST Catalog API. Implementations should ideally support both Iceberg table specs v1 and v2, with priority given to v2.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from polaris.catalog.models.assert_table_uuid import AssertTableUUID

class TestAssertTableUUID(unittest.TestCase):
    """AssertTableUUID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssertTableUUID:
        """Test AssertTableUUID
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssertTableUUID`
        """
        model = AssertTableUUID()
        if include_optional:
            return AssertTableUUID(
                type = 'assert-table-uuid',
                uuid = ''
            )
        else:
            return AssertTableUUID(
                type = 'assert-table-uuid',
                uuid = '',
        )
        """

    def testAssertTableUUID(self):
        """Test AssertTableUUID"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()