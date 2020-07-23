# kimai_python.TimesheetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_timesheets_active_get**](TimesheetApi.md#api_timesheets_active_get) | **GET** /api/timesheets/active | Returns the collection of active timesheet records
[**api_timesheets_get**](TimesheetApi.md#api_timesheets_get) | **GET** /api/timesheets | Returns a collection of timesheet records
[**api_timesheets_id_delete**](TimesheetApi.md#api_timesheets_id_delete) | **DELETE** /api/timesheets/{id} | Delete an existing timesheet record
[**api_timesheets_id_duplicate_patch**](TimesheetApi.md#api_timesheets_id_duplicate_patch) | **PATCH** /api/timesheets/{id}/duplicate | Duplicates an existing timesheet record
[**api_timesheets_id_export_patch**](TimesheetApi.md#api_timesheets_id_export_patch) | **PATCH** /api/timesheets/{id}/export | Switch the export state of a timesheet record to (un-)lock it
[**api_timesheets_id_get**](TimesheetApi.md#api_timesheets_id_get) | **GET** /api/timesheets/{id} | Returns one timesheet record
[**api_timesheets_id_meta_patch**](TimesheetApi.md#api_timesheets_id_meta_patch) | **PATCH** /api/timesheets/{id}/meta | Sets the value of a meta-field for an existing timesheet.
[**api_timesheets_id_patch**](TimesheetApi.md#api_timesheets_id_patch) | **PATCH** /api/timesheets/{id} | Update an existing timesheet record
[**api_timesheets_id_restart_patch**](TimesheetApi.md#api_timesheets_id_restart_patch) | **PATCH** /api/timesheets/{id}/restart | Restarts a previously stopped timesheet record for the current user
[**api_timesheets_id_stop_patch**](TimesheetApi.md#api_timesheets_id_stop_patch) | **PATCH** /api/timesheets/{id}/stop | Stops an active timesheet record
[**api_timesheets_post**](TimesheetApi.md#api_timesheets_post) | **POST** /api/timesheets | Creates a new timesheet record
[**api_timesheets_recent_get**](TimesheetApi.md#api_timesheets_recent_get) | **GET** /api/timesheets/recent | Returns the collection of recent user activities


# **api_timesheets_active_get**
> list[TimesheetCollectionExpanded] api_timesheets_active_get()

Returns the collection of active timesheet records

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))

try:
    # Returns the collection of active timesheet records
    api_response = api_instance.api_timesheets_active_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_active_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TimesheetCollectionExpanded]**](TimesheetCollectionExpanded.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_get**
> list[TimesheetCollection] api_timesheets_get(user=user, customer=customer, customers=customers, project=project, projects=projects, activity=activity, activities=activities, page=page, size=size, tags=tags, order_by=order_by, order=order, begin=begin, end=end, exported=exported, active=active, full=full, term=term, modified_after=modified_after)

Returns a collection of timesheet records

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
user = 'user_example' # str | User ID to filter timesheets. Needs permission 'view_other_timesheet', pass 'all' to fetch data for all user (default: current user) (optional)
customer = 'customer_example' # str | DEPRECATED: Customer ID to filter timesheets (will be removed with 2.0) (optional)
customers = 'customers_example' # str | Comma separated list of customer IDs to filter timesheets (optional)
project = 'project_example' # str | DEPRECATED: Project ID to filter timesheets (will be removed with 2.0) (optional)
projects = 'projects_example' # str | Comma separated list of project IDs to filter timesheets (optional)
activity = 'activity_example' # str | DEPRECATED: Activity ID to filter timesheets (will be removed with 2.0) (optional)
activities = 'activities_example' # str | Comma separated list of activity IDs to filter timesheets (optional)
page = 'page_example' # str | The page to display, renders a 404 if not found (default: 1) (optional)
size = 'size_example' # str | The amount of entries for each page (default: 50) (optional)
tags = 'tags_example' # str | The name of tags which are in the datasets (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, begin, end, rate (default: begin) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: DESC) (optional)
begin = 'begin_example' # str | Only records after this date will be included (format: HTML5) (optional)
end = 'end_example' # str | Only records before this date will be included (format: HTML5) (optional)
exported = 'exported_example' # str | Use this flag if you want to filter for export state. Allowed values: 0=not exported, 1=exported (default: all) (optional)
active = 'active_example' # str | Filter for running/active records. Allowed values: 0=stopped, 1=active (default: all) (optional)
full = 'full_example' # str | Allows to fetch fully serialized objects including subresources. Allowed values: true (default: false) (optional)
term = 'term_example' # str | Free search term (optional)
modified_after = 'modified_after_example' # str | Only records changed after this date will be included (format: HTML5). Available since Kimai 1.10 and works only for records that were created/updated since then. (optional)

try:
    # Returns a collection of timesheet records
    api_response = api_instance.api_timesheets_get(user=user, customer=customer, customers=customers, project=project, projects=projects, activity=activity, activities=activities, page=page, size=size, tags=tags, order_by=order_by, order=order, begin=begin, end=end, exported=exported, active=active, full=full, term=term, modified_after=modified_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User ID to filter timesheets. Needs permission &#39;view_other_timesheet&#39;, pass &#39;all&#39; to fetch data for all user (default: current user) | [optional] 
 **customer** | **str**| DEPRECATED: Customer ID to filter timesheets (will be removed with 2.0) | [optional] 
 **customers** | **str**| Comma separated list of customer IDs to filter timesheets | [optional] 
 **project** | **str**| DEPRECATED: Project ID to filter timesheets (will be removed with 2.0) | [optional] 
 **projects** | **str**| Comma separated list of project IDs to filter timesheets | [optional] 
 **activity** | **str**| DEPRECATED: Activity ID to filter timesheets (will be removed with 2.0) | [optional] 
 **activities** | **str**| Comma separated list of activity IDs to filter timesheets | [optional] 
 **page** | **str**| The page to display, renders a 404 if not found (default: 1) | [optional] 
 **size** | **str**| The amount of entries for each page (default: 50) | [optional] 
 **tags** | **str**| The name of tags which are in the datasets | [optional] 
 **order_by** | **str**| The field by which results will be ordered. Allowed values: id, begin, end, rate (default: begin) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: DESC) | [optional] 
 **begin** | **str**| Only records after this date will be included (format: HTML5) | [optional] 
 **end** | **str**| Only records before this date will be included (format: HTML5) | [optional] 
 **exported** | **str**| Use this flag if you want to filter for export state. Allowed values: 0&#x3D;not exported, 1&#x3D;exported (default: all) | [optional] 
 **active** | **str**| Filter for running/active records. Allowed values: 0&#x3D;stopped, 1&#x3D;active (default: all) | [optional] 
 **full** | **str**| Allows to fetch fully serialized objects including subresources. Allowed values: true (default: false) | [optional] 
 **term** | **str**| Free search term | [optional] 
 **modified_after** | **str**| Only records changed after this date will be included (format: HTML5). Available since Kimai 1.10 and works only for records that were created/updated since then. | [optional] 

### Return type

[**list[TimesheetCollection]**](TimesheetCollection.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_id_delete**
> api_timesheets_id_delete(id)

Delete an existing timesheet record

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
id = 56 # int | Timesheet record ID to delete

try:
    # Delete an existing timesheet record
    api_instance.api_timesheets_id_delete(id)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Timesheet record ID to delete | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_id_duplicate_patch**
> TimesheetEntity api_timesheets_id_duplicate_patch(id)

Duplicates an existing timesheet record

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
id = 56 # int | Timesheet record ID to duplicate

try:
    # Duplicates an existing timesheet record
    api_response = api_instance.api_timesheets_id_duplicate_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_id_duplicate_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Timesheet record ID to duplicate | 

### Return type

[**TimesheetEntity**](TimesheetEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_id_export_patch**
> TimesheetEntity api_timesheets_id_export_patch(id)

Switch the export state of a timesheet record to (un-)lock it

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
id = 56 # int | Timesheet record ID to switch export state

try:
    # Switch the export state of a timesheet record to (un-)lock it
    api_response = api_instance.api_timesheets_id_export_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_id_export_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Timesheet record ID to switch export state | 

### Return type

[**TimesheetEntity**](TimesheetEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_id_get**
> TimesheetEntity api_timesheets_id_get(id)

Returns one timesheet record

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
id = 56 # int | Timesheet record ID to fetch

try:
    # Returns one timesheet record
    api_response = api_instance.api_timesheets_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Timesheet record ID to fetch | 

### Return type

[**TimesheetEntity**](TimesheetEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_id_meta_patch**
> TimesheetEntity api_timesheets_id_meta_patch(id, body=body)

Sets the value of a meta-field for an existing timesheet.

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
id = 56 # int | Timesheet record ID to set the meta-field value for
body = kimai_python.Body4() # Body4 |  (optional)

try:
    # Sets the value of a meta-field for an existing timesheet.
    api_response = api_instance.api_timesheets_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_id_meta_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Timesheet record ID to set the meta-field value for | 
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**TimesheetEntity**](TimesheetEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_id_patch**
> TimesheetEntity api_timesheets_id_patch(body, id)

Update an existing timesheet record

Update an existing timesheet record, you can pass all or just a subset of the attributes.

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
body = kimai_python.TimesheetEditForm() # TimesheetEditForm | 
id = 56 # int | Timesheet record ID to update

try:
    # Update an existing timesheet record
    api_response = api_instance.api_timesheets_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimesheetEditForm**](TimesheetEditForm.md)|  | 
 **id** | **int**| Timesheet record ID to update | 

### Return type

[**TimesheetEntity**](TimesheetEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_id_restart_patch**
> TimesheetEntity api_timesheets_id_restart_patch(id, body=body)

Restarts a previously stopped timesheet record for the current user

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
id = 56 # int | Timesheet record ID to restart
body = kimai_python.Body3() # Body3 |  (optional)

try:
    # Restarts a previously stopped timesheet record for the current user
    api_response = api_instance.api_timesheets_id_restart_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_id_restart_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Timesheet record ID to restart | 
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**TimesheetEntity**](TimesheetEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_id_stop_patch**
> TimesheetEntity api_timesheets_id_stop_patch(id)

Stops an active timesheet record

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
id = 56 # int | Timesheet record ID to stop

try:
    # Stops an active timesheet record
    api_response = api_instance.api_timesheets_id_stop_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_id_stop_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Timesheet record ID to stop | 

### Return type

[**TimesheetEntity**](TimesheetEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_post**
> TimesheetEntity api_timesheets_post(body)

Creates a new timesheet record

Creates a new timesheet record for the current user and returns it afterwards.

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
body = kimai_python.TimesheetEditForm() # TimesheetEditForm | 

try:
    # Creates a new timesheet record
    api_response = api_instance.api_timesheets_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimesheetEditForm**](TimesheetEditForm.md)|  | 

### Return type

[**TimesheetEntity**](TimesheetEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_recent_get**
> list[TimesheetCollectionExpanded] api_timesheets_recent_get(user=user, begin=begin, size=size)

Returns the collection of recent user activities

### Example
```python
from __future__ import print_function
import time
import kimai_python
from kimai_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
user = 'user_example' # str | User ID to filter timesheets. Needs permission 'view_other_timesheet', pass 'all' to fetch data for all user (default: current user) (optional)
begin = 'begin_example' # str | Only records after this date will be included. Default: today - 1 year (format: HTML5) (optional)
size = 'size_example' # str | The amount of entries (default: 10) (optional)

try:
    # Returns the collection of recent user activities
    api_response = api_instance.api_timesheets_recent_get(user=user, begin=begin, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApi->api_timesheets_recent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User ID to filter timesheets. Needs permission &#39;view_other_timesheet&#39;, pass &#39;all&#39; to fetch data for all user (default: current user) | [optional] 
 **begin** | **str**| Only records after this date will be included. Default: today - 1 year (format: HTML5) | [optional] 
 **size** | **str**| The amount of entries (default: 10) | [optional] 

### Return type

[**list[TimesheetCollectionExpanded]**](TimesheetCollectionExpanded.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

