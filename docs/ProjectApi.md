# kimai_python.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_projects_get**](ProjectApi.md#api_projects_get) | **GET** /api/projects | Returns a collection of projects.
[**api_projects_id_get**](ProjectApi.md#api_projects_id_get) | **GET** /api/projects/{id} | Returns one project
[**api_projects_id_meta_patch**](ProjectApi.md#api_projects_id_meta_patch) | **PATCH** /api/projects/{id}/meta | Sets the value of a meta-field for an existing project
[**api_projects_id_patch**](ProjectApi.md#api_projects_id_patch) | **PATCH** /api/projects/{id} | Update an existing project
[**api_projects_id_rates_get**](ProjectApi.md#api_projects_id_rates_get) | **GET** /api/projects/{id}/rates | Returns a collection of all rates for one project
[**api_projects_id_rates_post**](ProjectApi.md#api_projects_id_rates_post) | **POST** /api/projects/{id}/rates | Adds a new rate to an project
[**api_projects_id_rates_rate_id_delete**](ProjectApi.md#api_projects_id_rates_rate_id_delete) | **DELETE** /api/projects/{id}/rates/{rateId} | Deletes one rate for an project
[**api_projects_post**](ProjectApi.md#api_projects_post) | **POST** /api/projects | Creates a new project


# **api_projects_get**
> list[ProjectCollection] api_projects_get(customer=customer, customers=customers, visible=visible, start=start, end=end, ignore_dates=ignore_dates, order=order, order_by=order_by, term=term)

Returns a collection of projects.

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
api_instance = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
customer = 'customer_example' # str | Customer ID to filter projects (optional)
customers = 'customers_example' # str | Comma separated list of customer IDs to filter projects (optional)
visible = 'visible_example' # str | Visibility status to filter projects. Allowed values: 1=visible, 2=hidden, 3=both (default: 1) (optional)
start = 'start_example' # str | Only projects that started before this date will be included. Allowed format: HTML5 (default: now, if end is also empty) (optional)
end = 'end_example' # str | Only projects that ended after this date will be included. Allowed format: HTML5 (default: now, if start is also empty) (optional)
ignore_dates = 'ignore_dates_example' # str | If set, start and end are completely ignored. Allowed values: 1 (default: off) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: ASC) (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, name, customer (default: name) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns a collection of projects.
    api_response = api_instance.api_projects_get(customer=customer, customers=customers, visible=visible, start=start, end=end, ignore_dates=ignore_dates, order=order, order_by=order_by, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | **str**| Customer ID to filter projects | [optional] 
 **customers** | **str**| Comma separated list of customer IDs to filter projects | [optional] 
 **visible** | **str**| Visibility status to filter projects. Allowed values: 1&#x3D;visible, 2&#x3D;hidden, 3&#x3D;both (default: 1) | [optional] 
 **start** | **str**| Only projects that started before this date will be included. Allowed format: HTML5 (default: now, if end is also empty) | [optional] 
 **end** | **str**| Only projects that ended after this date will be included. Allowed format: HTML5 (default: now, if start is also empty) | [optional] 
 **ignore_dates** | **str**| If set, start and end are completely ignored. Allowed values: 1 (default: off) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: ASC) | [optional] 
 **order_by** | **str**| The field by which results will be ordered. Allowed values: id, name, customer (default: name) | [optional] 
 **term** | **str**| Free search term | [optional] 

### Return type

[**list[ProjectCollection]**](ProjectCollection.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_id_get**
> ProjectEntity api_projects_id_get(id)

Returns one project

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
api_instance = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns one project
    api_response = api_instance.api_projects_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_projects_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectEntity**](ProjectEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_id_meta_patch**
> ProjectEntity api_projects_id_meta_patch(id, body=body)

Sets the value of a meta-field for an existing project

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
api_instance = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
id = 56 # int | Project record ID to set the meta-field value for
body = kimai_python.Body2() # Body2 |  (optional)

try:
    # Sets the value of a meta-field for an existing project
    api_response = api_instance.api_projects_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_projects_id_meta_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Project record ID to set the meta-field value for | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**ProjectEntity**](ProjectEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_id_patch**
> ProjectEntity api_projects_id_patch(body, id)

Update an existing project

Update an existing project, you can pass all or just a subset of all attributes

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
api_instance = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
body = kimai_python.ProjectEditForm() # ProjectEditForm | 
id = 56 # int | Project ID to update

try:
    # Update an existing project
    api_response = api_instance.api_projects_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_projects_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectEditForm**](ProjectEditForm.md)|  | 
 **id** | **int**| Project ID to update | 

### Return type

[**ProjectEntity**](ProjectEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_id_rates_get**
> list[ProjectRate] api_projects_id_rates_get(id)

Returns a collection of all rates for one project

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
api_instance = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
id = 56 # int | The project whose rates will be returned

try:
    # Returns a collection of all rates for one project
    api_response = api_instance.api_projects_id_rates_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_projects_id_rates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project whose rates will be returned | 

### Return type

[**list[ProjectRate]**](ProjectRate.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_id_rates_post**
> ProjectRate api_projects_id_rates_post(id, body)

Adds a new rate to an project

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
api_instance = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
id = 56 # int | The project to add the rate for
body = kimai_python.ProjectRateForm() # ProjectRateForm | 

try:
    # Adds a new rate to an project
    api_response = api_instance.api_projects_id_rates_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_projects_id_rates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project to add the rate for | 
 **body** | [**ProjectRateForm**](ProjectRateForm.md)|  | 

### Return type

[**ProjectRate**](ProjectRate.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_id_rates_rate_id_delete**
> api_projects_id_rates_rate_id_delete(id, rate_id)

Deletes one rate for an project

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
api_instance = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
id = 56 # int | The project whose rate will be removed
rate_id = 56 # int | The rate to remove

try:
    # Deletes one rate for an project
    api_instance.api_projects_id_rates_rate_id_delete(id, rate_id)
except ApiException as e:
    print("Exception when calling ProjectApi->api_projects_id_rates_rate_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project whose rate will be removed | 
 **rate_id** | **int**| The rate to remove | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_post**
> ProjectEntity api_projects_post(body)

Creates a new project

Creates a new project and returns it afterwards

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
api_instance = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
body = kimai_python.ProjectEditForm() # ProjectEditForm | 

try:
    # Creates a new project
    api_response = api_instance.api_projects_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectEditForm**](ProjectEditForm.md)|  | 

### Return type

[**ProjectEntity**](ProjectEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

