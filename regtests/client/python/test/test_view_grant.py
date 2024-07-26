# coding: utf-8

"""
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from polaris.management.models.view_grant import ViewGrant

class TestViewGrant(unittest.TestCase):
    """ViewGrant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ViewGrant:
        """Test ViewGrant
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ViewGrant`
        """
        model = ViewGrant()
        if include_optional:
            return ViewGrant(
                namespace = [
                    ''
                    ],
                view_name = '',
                privilege = 'CATALOG_MANAGE_ACCESS'
            )
        else:
            return ViewGrant(
                namespace = [
                    ''
                    ],
                view_name = '',
                privilege = 'CATALOG_MANAGE_ACCESS',
        )
        """

    def testViewGrant(self):
        """Test ViewGrant"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()