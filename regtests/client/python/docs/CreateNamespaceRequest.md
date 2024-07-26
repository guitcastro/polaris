# CreateNamespaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **List[str]** | Reference to one or more levels of a namespace | 
**properties** | **Dict[str, str]** | Configured string to string map of properties for the namespace | [optional] 

## Example

```python
from polaris.catalog.models.create_namespace_request import CreateNamespaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNamespaceRequest from a JSON string
create_namespace_request_instance = CreateNamespaceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNamespaceRequest.to_json())

# convert the object into a dict
create_namespace_request_dict = create_namespace_request_instance.to_dict()
# create an instance of CreateNamespaceRequest from a dict
create_namespace_request_from_dict = CreateNamespaceRequest.from_dict(create_namespace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

