# swagger_client.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_users_get**](UserApi.md#api_users_get) | **GET** /api/users | Returns the collection of all registered users
[**api_users_id_get**](UserApi.md#api_users_id_get) | **GET** /api/users/{id} | Return one user entity
[**api_users_id_patch**](UserApi.md#api_users_id_patch) | **PATCH** /api/users/{id} | Update an existing user
[**api_users_me_get**](UserApi.md#api_users_me_get) | **GET** /api/users/me | Return the current user entity
[**api_users_post**](UserApi.md#api_users_post) | **POST** /api/users | Creates a new user


# **api_users_get**
> list[UserCollection] api_users_get(visible=visible, order_by=order_by, order=order, term=term)

Returns the collection of all registered users

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
visible = 'visible_example' # str | Visibility status to filter users. Allowed values: 1=visible, 2=hidden, 3=all (default: 1) (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, username, alias, email (default: username) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: ASC) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns the collection of all registered users
    api_response = api_instance.api_users_get(visible=visible, order_by=order_by, order=order, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->api_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visible** | **str**| Visibility status to filter users. Allowed values: 1&#x3D;visible, 2&#x3D;hidden, 3&#x3D;all (default: 1) | [optional] 
 **order_by** | **str**| The field by which results will be ordered. Allowed values: id, username, alias, email (default: username) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: ASC) | [optional] 
 **term** | **str**| Free search term | [optional] 

### Return type

[**list[UserCollection]**](UserCollection.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_get**
> UserEntity api_users_id_get(id)

Return one user entity

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = 56 # int | User ID to fetch

try:
    # Return one user entity
    api_response = api_instance.api_users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->api_users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID to fetch | 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_patch**
> UserEntity api_users_id_patch(body, id)

Update an existing user

Update an existing user, you can pass all or just a subset of all attributes (passing roles will replace all existing ones)

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserEditForm() # UserEditForm | 
id = 56 # int | User ID to update

try:
    # Update an existing user
    api_response = api_instance.api_users_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->api_users_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserEditForm**](UserEditForm.md)|  | 
 **id** | **int**| User ID to update | 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_me_get**
> UserEntity api_users_me_get()

Return the current user entity

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # Return the current user entity
    api_response = api_instance.api_users_me_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->api_users_me_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_post**
> UserEntity api_users_post(body)

Creates a new user

Creates a new user and returns it afterwards

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCreateForm() # UserCreateForm | 

try:
    # Creates a new user
    api_response = api_instance.api_users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->api_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateForm**](UserCreateForm.md)|  | 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

