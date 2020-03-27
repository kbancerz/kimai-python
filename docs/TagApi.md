# swagger_client.TagApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tags_get**](TagApi.md#api_tags_get) | **GET** /api/tags | Fetch all existing tags
[**api_tags_id_delete**](TagApi.md#api_tags_id_delete) | **DELETE** /api/tags/{id} | Delete a tag
[**api_tags_post**](TagApi.md#api_tags_post) | **POST** /api/tags | Creates a new tag


# **api_tags_get**
> list[str] api_tags_get(name=name)

Fetch all existing tags

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Search term to filter tag list (optional)

try:
    # Fetch all existing tags
    api_response = api_instance.api_tags_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->api_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search term to filter tag list | [optional] 

### Return type

**list[str]**

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tags_id_delete**
> api_tags_id_delete(id)

Delete a tag

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
id = 56 # int | Tag ID to delete

try:
    # Delete a tag
    api_instance.api_tags_id_delete(id)
except ApiException as e:
    print("Exception when calling TagApi->api_tags_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tag ID to delete | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tags_post**
> TagEntity api_tags_post(body)

Creates a new tag

Creates a new tag and returns it afterwards

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
body = swagger_client.TagEditForm() # TagEditForm | 

try:
    # Creates a new tag
    api_response = api_instance.api_tags_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->api_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagEditForm**](TagEditForm.md)|  | 

### Return type

[**TagEntity**](TagEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

