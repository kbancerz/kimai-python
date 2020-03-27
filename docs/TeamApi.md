# swagger_client.TeamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_teams_get**](TeamApi.md#api_teams_get) | **GET** /api/teams | Fetch all existing teams
[**api_teams_id_customers_customer_id_delete**](TeamApi.md#api_teams_id_customers_customer_id_delete) | **DELETE** /api/teams/{id}/customers/{customerId} | Revokes access for a customer from a team
[**api_teams_id_customers_customer_id_post**](TeamApi.md#api_teams_id_customers_customer_id_post) | **POST** /api/teams/{id}/customers/{customerId} | Grant the team access to a customer
[**api_teams_id_delete**](TeamApi.md#api_teams_id_delete) | **DELETE** /api/teams/{id} | Delete a team
[**api_teams_id_get**](TeamApi.md#api_teams_id_get) | **GET** /api/teams/{id} | Returns one team
[**api_teams_id_members_user_id_delete**](TeamApi.md#api_teams_id_members_user_id_delete) | **DELETE** /api/teams/{id}/members/{userId} | Removes a member from the team
[**api_teams_id_members_user_id_post**](TeamApi.md#api_teams_id_members_user_id_post) | **POST** /api/teams/{id}/members/{userId} | Add a new member to a team
[**api_teams_id_patch**](TeamApi.md#api_teams_id_patch) | **PATCH** /api/teams/{id} | Update an existing team
[**api_teams_id_projects_project_id_delete**](TeamApi.md#api_teams_id_projects_project_id_delete) | **DELETE** /api/teams/{id}/projects/{projectId} | Revokes access for a project from a team
[**api_teams_id_projects_project_id_post**](TeamApi.md#api_teams_id_projects_project_id_post) | **POST** /api/teams/{id}/projects/{projectId} | Grant the team access to a project
[**api_teams_post**](TeamApi.md#api_teams_post) | **POST** /api/teams | Creates a new team


# **api_teams_get**
> list[TeamCollection] api_teams_get()

Fetch all existing teams

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))

try:
    # Fetch all existing teams
    api_response = api_instance.api_teams_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TeamCollection]**](TeamCollection.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_customers_customer_id_delete**
> TeamEntity api_teams_id_customers_customer_id_delete(id, customer_id)

Revokes access for a customer from a team

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team whose permission will be revoked
customer_id = 56 # int | The customer to remove (Customer ID)

try:
    # Revokes access for a customer from a team
    api_response = api_instance.api_teams_id_customers_customer_id_delete(id, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_customers_customer_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The team whose permission will be revoked | 
 **customer_id** | **int**| The customer to remove (Customer ID) | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_customers_customer_id_post**
> TeamEntity api_teams_id_customers_customer_id_post(id, customer_id)

Grant the team access to a customer

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team that is granted access
customer_id = 56 # int | The customer to grant acecess to (Customer ID)

try:
    # Grant the team access to a customer
    api_response = api_instance.api_teams_id_customers_customer_id_post(id, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_customers_customer_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The team that is granted access | 
 **customer_id** | **int**| The customer to grant acecess to (Customer ID) | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_delete**
> api_teams_id_delete(id)

Delete a team

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
id = 56 # int | Team ID to delete

try:
    # Delete a team
    api_instance.api_teams_id_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Team ID to delete | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_get**
> TeamEntity api_teams_id_get(id)

Returns one team

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns one team
    api_response = api_instance.api_teams_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_members_user_id_delete**
> TeamEntity api_teams_id_members_user_id_delete(id, user_id)

Removes a member from the team

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team from which the member will be removed
user_id = 56 # int | The team member to remove (User ID)

try:
    # Removes a member from the team
    api_response = api_instance.api_teams_id_members_user_id_delete(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_members_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The team from which the member will be removed | 
 **user_id** | **int**| The team member to remove (User ID) | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_members_user_id_post**
> TeamEntity api_teams_id_members_user_id_post(id, user_id)

Add a new member to a team

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team which will receive the new member
user_id = 56 # int | The team member to add (User ID)

try:
    # Add a new member to a team
    api_response = api_instance.api_teams_id_members_user_id_post(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_members_user_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The team which will receive the new member | 
 **user_id** | **int**| The team member to add (User ID) | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_patch**
> TeamEntity api_teams_id_patch(body, id)

Update an existing team

Update an existing team, you can pass all or just a subset of all attributes (passing users will replace all existing ones)

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
body = swagger_client.TeamEditForm() # TeamEditForm | 
id = 56 # int | Team ID to update

try:
    # Update an existing team
    api_response = api_instance.api_teams_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamEditForm**](TeamEditForm.md)|  | 
 **id** | **int**| Team ID to update | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_projects_project_id_delete**
> TeamEntity api_teams_id_projects_project_id_delete(id, project_id)

Revokes access for a project from a team

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team whose permission will be revoked
project_id = 56 # int | The project to remove (Project ID)

try:
    # Revokes access for a project from a team
    api_response = api_instance.api_teams_id_projects_project_id_delete(id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_projects_project_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The team whose permission will be revoked | 
 **project_id** | **int**| The project to remove (Project ID) | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_id_projects_project_id_post**
> TeamEntity api_teams_id_projects_project_id_post(id, project_id)

Grant the team access to a project

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team that is granted access
project_id = 56 # int | The project to grant acecess to (Project ID)

try:
    # Grant the team access to a project
    api_response = api_instance.api_teams_id_projects_project_id_post(id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_id_projects_project_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The team that is granted access | 
 **project_id** | **int**| The project to grant acecess to (Project ID) | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_teams_post**
> TeamEntity api_teams_post(body)

Creates a new team

Creates a new team and returns it afterwards

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
api_instance = swagger_client.TeamApi(swagger_client.ApiClient(configuration))
body = swagger_client.TeamEditForm() # TeamEditForm | 

try:
    # Creates a new team
    api_response = api_instance.api_teams_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->api_teams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamEditForm**](TeamEditForm.md)|  | 

### Return type

[**TeamEntity**](TeamEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

