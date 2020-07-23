# ProjectEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_title** | **str** |  | [optional] 
**customer** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**order_number** | **str** |  | [optional] 
**order_date** | **datetime** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**comment** | **str** |  | [optional] 
**visible** | **bool** |  | 
**budget** | **float** |  | 
**time_budget** | **int** |  | 
**meta_fields** | [**list[ProjectMeta]**](ProjectMeta.md) | All visible meta (custom) fields registered with this project | [optional] 
**teams** | [**list[Team]**](Team.md) | If no team is assigned, everyone can access the project (also depends on the teams of the customer) | [optional] 
**color** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


