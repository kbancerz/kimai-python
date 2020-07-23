# TimesheetCollectionExpanded

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**begin** | **datetime** |  | 
**end** | **datetime** |  | [optional] 
**duration** | **int** |  | [optional] 
**activity** | [**list[ActivityExpanded]**](ActivityExpanded.md) |  | 
**project** | [**list[ProjectExpanded]**](ProjectExpanded.md) |  | 
**description** | **str** |  | [optional] 
**rate** | **float** |  | [optional] 
**internal_rate** | **float** |  | [optional] 
**meta_fields** | [**list[TimesheetMeta]**](TimesheetMeta.md) | All visible meta (custom) fields registered with this timesheet | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


