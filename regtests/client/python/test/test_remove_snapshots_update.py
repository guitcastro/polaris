# coding: utf-8

"""
    Apache Iceberg REST Catalog API

    Defines the specification for the first version of the REST Catalog API. Implementations should ideally support both Iceberg table specs v1 and v2, with priority given to v2.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from polaris.catalog.models.remove_snapshots_update import RemoveSnapshotsUpdate

class TestRemoveSnapshotsUpdate(unittest.TestCase):
    """RemoveSnapshotsUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoveSnapshotsUpdate:
        """Test RemoveSnapshotsUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoveSnapshotsUpdate`
        """
        model = RemoveSnapshotsUpdate()
        if include_optional:
            return RemoveSnapshotsUpdate(
                action = 'remove-snapshots',
                snapshot_ids = [
                    56
                    ]
            )
        else:
            return RemoveSnapshotsUpdate(
                action = 'remove-snapshots',
                snapshot_ids = [
                    56
                    ],
        )
        """

    def testRemoveSnapshotsUpdate(self):
        """Test RemoveSnapshotsUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()