# swagger_client.ActivityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_activities_get**](ActivityApi.md#api_activities_get) | **GET** /api/activities | Returns a collection of activities
[**api_activities_id_get**](ActivityApi.md#api_activities_id_get) | **GET** /api/activities/{id} | Returns one activity
[**api_activities_id_meta_patch**](ActivityApi.md#api_activities_id_meta_patch) | **PATCH** /api/activities/{id}/meta | Sets the value of a meta-field for an existing activity
[**api_activities_id_patch**](ActivityApi.md#api_activities_id_patch) | **PATCH** /api/activities/{id} | Update an existing activity
[**api_activities_id_rates_get**](ActivityApi.md#api_activities_id_rates_get) | **GET** /api/activities/{id}/rates | Returns a collection of all rates for one activity
[**api_activities_id_rates_post**](ActivityApi.md#api_activities_id_rates_post) | **POST** /api/activities/{id}/rates | Adds a new rate to an activity
[**api_activities_id_rates_rate_id_delete**](ActivityApi.md#api_activities_id_rates_rate_id_delete) | **DELETE** /api/activities/{id}/rates/{rateId} | Deletes one rate for an activity
[**api_activities_post**](ActivityApi.md#api_activities_post) | **POST** /api/activities | Creates a new activity


# **api_activities_get**
> list[ActivityCollection] api_activities_get(project=project, projects=projects, visible=visible, globals=globals, globals_first=globals_first, order_by=order_by, order=order, term=term)

Returns a collection of activities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
project = 'project_example' # str | Project ID to filter activities (optional)
projects = 'projects_example' # str | Comma separated list of project IDs to filter activities (optional)
visible = 'visible_example' # str | Visibility status to filter activities. Allowed values: 1=visible, 2=hidden, 3=all (default: 1) (optional)
globals = 'globals_example' # str | Use if you want to fetch only global activities. Allowed values: true (default: false) (optional)
globals_first = 'globals_first_example' # str | Deprecated parameter, value is not used any more (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, name, project (default: name) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: ASC) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns a collection of activities
    api_response = api_instance.api_activities_get(project=project, projects=projects, visible=visible, globals=globals, globals_first=globals_first, order_by=order_by, order=order, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->api_activities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project ID to filter activities | [optional] 
 **projects** | **str**| Comma separated list of project IDs to filter activities | [optional] 
 **visible** | **str**| Visibility status to filter activities. Allowed values: 1&#x3D;visible, 2&#x3D;hidden, 3&#x3D;all (default: 1) | [optional] 
 **globals** | **str**| Use if you want to fetch only global activities. Allowed values: true (default: false) | [optional] 
 **globals_first** | **str**| Deprecated parameter, value is not used any more | [optional] 
 **order_by** | **str**| The field by which results will be ordered. Allowed values: id, name, project (default: name) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: ASC) | [optional] 
 **term** | **str**| Free search term | [optional] 

### Return type

[**list[ActivityCollection]**](ActivityCollection.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activities_id_get**
> ActivityEntity api_activities_id_get(id)

Returns one activity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
id = 56 # int | Activity ID to fetch

try:
    # Returns one activity
    api_response = api_instance.api_activities_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->api_activities_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Activity ID to fetch | 

### Return type

[**ActivityEntity**](ActivityEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activities_id_meta_patch**
> ActivityEntity api_activities_id_meta_patch(id, body=body)

Sets the value of a meta-field for an existing activity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
id = 56 # int | Activity record ID to set the meta-field value for
body = swagger_client.Body() # Body |  (optional)

try:
    # Sets the value of a meta-field for an existing activity
    api_response = api_instance.api_activities_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->api_activities_id_meta_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Activity record ID to set the meta-field value for | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**ActivityEntity**](ActivityEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activities_id_patch**
> ActivityEntity api_activities_id_patch(body, id)

Update an existing activity

Update an existing activity, you can pass all or just a subset of all attributes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
body = swagger_client.ActivityEditForm() # ActivityEditForm | 
id = 56 # int | Activity ID to update

try:
    # Update an existing activity
    api_response = api_instance.api_activities_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->api_activities_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActivityEditForm**](ActivityEditForm.md)|  | 
 **id** | **int**| Activity ID to update | 

### Return type

[**ActivityEntity**](ActivityEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activities_id_rates_get**
> list[ActivityRate] api_activities_id_rates_get(id)

Returns a collection of all rates for one activity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
id = 56 # int | The activity whose rates will be returned

try:
    # Returns a collection of all rates for one activity
    api_response = api_instance.api_activities_id_rates_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->api_activities_id_rates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The activity whose rates will be returned | 

### Return type

[**list[ActivityRate]**](ActivityRate.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activities_id_rates_post**
> ActivityRate api_activities_id_rates_post(id, body)

Adds a new rate to an activity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
id = 56 # int | The activity to add the rate for
body = swagger_client.ActivityRateForm() # ActivityRateForm | 

try:
    # Adds a new rate to an activity
    api_response = api_instance.api_activities_id_rates_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->api_activities_id_rates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The activity to add the rate for | 
 **body** | [**ActivityRateForm**](ActivityRateForm.md)|  | 

### Return type

[**ActivityRate**](ActivityRate.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activities_id_rates_rate_id_delete**
> api_activities_id_rates_rate_id_delete(id, rate_id)

Deletes one rate for an activity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
id = 56 # int | The activity whose rate will be removed
rate_id = 56 # int | The rate to remove

try:
    # Deletes one rate for an activity
    api_instance.api_activities_id_rates_rate_id_delete(id, rate_id)
except ApiException as e:
    print("Exception when calling ActivityApi->api_activities_id_rates_rate_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The activity whose rate will be removed | 
 **rate_id** | **int**| The rate to remove | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_activities_post**
> ActivityEntity api_activities_post(body)

Creates a new activity

Creates a new activity and returns it afterwards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiToken
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'
# Configure API key authorization: apiUser
configuration = swagger_client.Configuration()
configuration.api_key['X-AUTH-USER'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-USER'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
body = swagger_client.ActivityEditForm() # ActivityEditForm | 

try:
    # Creates a new activity
    api_response = api_instance.api_activities_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->api_activities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActivityEditForm**](ActivityEditForm.md)|  | 

### Return type

[**ActivityEntity**](ActivityEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

