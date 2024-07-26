# SetSnapshotRefUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**ref_name** | **str** |  | 
**type** | **str** |  | 
**snapshot_id** | **int** |  | 
**max_ref_age_ms** | **int** |  | [optional] 
**max_snapshot_age_ms** | **int** |  | [optional] 
**min_snapshots_to_keep** | **int** |  | [optional] 

## Example

```python
from polaris.catalog.models.set_snapshot_ref_update import SetSnapshotRefUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SetSnapshotRefUpdate from a JSON string
set_snapshot_ref_update_instance = SetSnapshotRefUpdate.from_json(json)
# print the JSON string representation of the object
print(SetSnapshotRefUpdate.to_json())

# convert the object into a dict
set_snapshot_ref_update_dict = set_snapshot_ref_update_instance.to_dict()
# create an instance of SetSnapshotRefUpdate from a dict
set_snapshot_ref_update_from_dict = SetSnapshotRefUpdate.from_dict(set_snapshot_ref_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

