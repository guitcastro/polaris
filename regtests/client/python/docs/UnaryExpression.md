# UnaryExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**term** | [**Term**](Term.md) |  | 
**value** | **object** |  | 

## Example

```python
from polaris.catalog.models.unary_expression import UnaryExpression

# TODO update the JSON string below
json = "{}"
# create an instance of UnaryExpression from a JSON string
unary_expression_instance = UnaryExpression.from_json(json)
# print the JSON string representation of the object
print(UnaryExpression.to_json())

# convert the object into a dict
unary_expression_dict = unary_expression_instance.to_dict()
# create an instance of UnaryExpression from a dict
unary_expression_from_dict = UnaryExpression.from_dict(unary_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

