# coding: utf-8

"""
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CatalogRole(BaseModel):
    """
    CatalogRole
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the role")
    properties: Optional[Dict[str, StrictStr]] = None
    create_timestamp: Optional[StrictInt] = Field(default=None, alias="createTimestamp")
    last_update_timestamp: Optional[StrictInt] = Field(default=None, alias="lastUpdateTimestamp")
    entity_version: Optional[StrictInt] = Field(default=None, description="The version of the catalog role object used to determine if the catalog role metadata has changed", alias="entityVersion")
    __properties: ClassVar[List[str]] = ["name", "properties", "createTimestamp", "lastUpdateTimestamp", "entityVersion"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CatalogRole from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CatalogRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "properties": obj.get("properties"),
            "createTimestamp": obj.get("createTimestamp"),
            "lastUpdateTimestamp": obj.get("lastUpdateTimestamp"),
            "entityVersion": obj.get("entityVersion")
        })
        return _obj

