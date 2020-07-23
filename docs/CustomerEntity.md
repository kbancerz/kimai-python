# CustomerEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**number** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**visible** | **bool** |  | 
**company** | **str** |  | [optional] 
**vat_id** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**country** | **str** |  | 
**currency** | **str** |  | 
**phone** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**email** | **str** | Limited via RFC to 254 chars | [optional] 
**homepage** | **str** |  | [optional] 
**timezone** | **str** | Length was determined by a MySQL column via \&quot;use mysql;describe time_zone_name;\&quot; | 
**budget** | **float** |  | 
**time_budget** | **int** |  | 
**meta_fields** | [**list[CustomerMeta]**](CustomerMeta.md) | All visible meta (custom) fields registered with this customer | [optional] 
**teams** | [**list[Team]**](Team.md) | If no team is assigned, everyone can access the customer | [optional] 
**color** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


