# coding: utf-8

"""
    Apache Iceberg REST Catalog API

    Defines the specification for the first version of the REST Catalog API. Implementations should ideally support both Iceberg table specs v1 and v2, with priority given to v2.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from polaris.catalog.models.type import Type

class TestType(unittest.TestCase):
    """Type unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Type:
        """Test Type
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Type`
        """
        model = Type()
        if include_optional:
            return Type(
                type = 'struct',
                fields = [
                    polaris.catalog.models.struct_field.StructField(
                        id = 56, 
                        name = '', 
                        type = null, 
                        required = True, 
                        doc = '', )
                    ],
                element_id = 56,
                element = None,
                element_required = True,
                key_id = 56,
                key = None,
                value_id = 56,
                value = None,
                value_required = True
            )
        else:
            return Type(
                type = 'struct',
                fields = [
                    polaris.catalog.models.struct_field.StructField(
                        id = 56, 
                        name = '', 
                        type = null, 
                        required = True, 
                        doc = '', )
                    ],
                element_id = 56,
                element = None,
                element_required = True,
                key_id = 56,
                key = None,
                value_id = 56,
                value = None,
                value_required = True,
        )
        """

    def testType(self):
        """Test Type"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()