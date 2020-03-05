# swagger_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_activities_get**](DefaultApi.md#api_activities_get) | **GET** /api/activities | Returns a collection of activities
[**api_activities_id_get**](DefaultApi.md#api_activities_id_get) | **GET** /api/activities/{id} | Returns one activity
[**api_activities_id_meta_patch**](DefaultApi.md#api_activities_id_meta_patch) | **PATCH** /api/activities/{id}/meta | Sets the value of a meta-field for an existing activity.
[**api_activities_id_patch**](DefaultApi.md#api_activities_id_patch) | **PATCH** /api/activities/{id} | Update an existing activity
[**api_activities_post**](DefaultApi.md#api_activities_post) | **POST** /api/activities | Creates a new activity
[**api_config_i18n_get**](DefaultApi.md#api_config_i18n_get) | **GET** /api/config/i18n | Returns the user specific locale configuration
[**api_config_timesheet_get**](DefaultApi.md#api_config_timesheet_get) | **GET** /api/config/timesheet | Returns the instance specific timesheet configuration
[**api_customers_get**](DefaultApi.md#api_customers_get) | **GET** /api/customers | Returns a collection of customers
[**api_customers_id_get**](DefaultApi.md#api_customers_id_get) | **GET** /api/customers/{id} | Returns one customer
[**api_customers_id_meta_patch**](DefaultApi.md#api_customers_id_meta_patch) | **PATCH** /api/customers/{id}/meta | Sets the value of a meta-field for an existing customer.
[**api_customers_id_patch**](DefaultApi.md#api_customers_id_patch) | **PATCH** /api/customers/{id} | Update an existing customer
[**api_customers_post**](DefaultApi.md#api_customers_post) | **POST** /api/customers | Creates a new customer
[**api_ping_get**](DefaultApi.md#api_ping_get) | **GET** /api/ping | A testing route for the API
[**api_projects_get**](DefaultApi.md#api_projects_get) | **GET** /api/projects | Returns a collection of projects.
[**api_projects_id_get**](DefaultApi.md#api_projects_id_get) | **GET** /api/projects/{id} | Returns one project
[**api_projects_id_meta_patch**](DefaultApi.md#api_projects_id_meta_patch) | **PATCH** /api/projects/{id}/meta | Sets the value of a meta-field for an existing project.
[**api_projects_id_patch**](DefaultApi.md#api_projects_id_patch) | **PATCH** /api/projects/{id} | Update an existing project
[**api_projects_post**](DefaultApi.md#api_projects_post) | **POST** /api/projects | Creates a new project
[**api_tags_get**](DefaultApi.md#api_tags_get) | **GET** /api/tags | Fetch all existing tags
[**api_tags_id_delete**](DefaultApi.md#api_tags_id_delete) | **DELETE** /api/tags/{id} | Delete a tag
[**api_tags_post**](DefaultApi.md#api_tags_post) | **POST** /api/tags | Creates a new tag
[**api_teams_get**](DefaultApi.md#api_teams_get) | **GET** /api/teams | Fetch all existing teams
[**api_teams_id_customers_customer_id_delete**](DefaultApi.md#api_teams_id_customers_customer_id_delete) | **DELETE** /api/teams/{id}/customers/{customerId} | Revokes access for a customer from a team
[**api_teams_id_customers_customer_id_post**](DefaultApi.md#api_teams_id_customers_customer_id_post) | **POST** /api/teams/{id}/customers/{customerId} | Grant the team access to a customer
[**api_teams_id_delete**](DefaultApi.md#api_teams_id_delete) | **DELETE** /api/teams/{id} | Delete a team
[**api_teams_id_get**](DefaultApi.md#api_teams_id_get) | **GET** /api/teams/{id} | Returns one team
[**api_teams_id_members_user_id_delete**](DefaultApi.md#api_teams_id_members_user_id_delete) | **DELETE** /api/teams/{id}/members/{userId} | Removes a member from the team
[**api_teams_id_members_user_id_post**](DefaultApi.md#api_teams_id_members_user_id_post) | **POST** /api/teams/{id}/members/{userId} | Add a new member to a team
[**api_teams_id_patch**](DefaultApi.md#api_teams_id_patch) | **PATCH** /api/teams/{id} | Update an existing team
[**api_teams_id_projects_project_id_delete**](DefaultApi.md#api_teams_id_projects_project_id_delete) | **DELETE** /api/teams/{id}/projects/{projectId} | Revokes access for a project from a team
[**api_teams_id_projects_project_id_post**](DefaultApi.md#api_teams_id_projects_project_id_post) | **POST** /api/teams/{id}/projects/{projectId} | Grant the team access to a project
[**api_teams_post**](DefaultApi.md#api_teams_post) | **POST** /api/teams | Creates a new team
[**api_timesheets_active_get**](DefaultApi.md#api_timesheets_active_get) | **GET** /api/timesheets/active | Returns the collection of active timesheet records
[**api_timesheets_get**](DefaultApi.md#api_timesheets_get) | **GET** /api/timesheets | Returns a collection of timesheet records
[**api_timesheets_id_delete**](DefaultApi.md#api_timesheets_id_delete) | **DELETE** /api/timesheets/{id} | Delete an existing timesheet record
[**api_timesheets_id_duplicate_patch**](DefaultApi.md#api_timesheets_id_duplicate_patch) | **PATCH** /api/timesheets/{id}/duplicate | Duplicates an existing timesheet record
[**api_timesheets_id_export_patch**](DefaultApi.md#api_timesheets_id_export_patch) | **PATCH** /api/timesheets/{id}/export | Switch the export state of a timesheet record to (un-)lock it
[**api_timesheets_id_get**](DefaultApi.md#api_timesheets_id_get) | **GET** /api/timesheets/{id} | Returns one timesheet record
[**api_timesheets_id_meta_patch**](DefaultApi.md#api_timesheets_id_meta_patch) | **PATCH** /api/timesheets/{id}/meta | Sets the value of a meta-field for an existing timesheet.
[**api_timesheets_id_patch**](DefaultApi.md#api_timesheets_id_patch) | **PATCH** /api/timesheets/{id} | Update an existing timesheet record
[**api_timesheets_id_restart_patch**](DefaultApi.md#api_timesheets_id_restart_patch) | **PATCH** /api/timesheets/{id}/restart | Restarts a previously stopped timesheet record for the current user
[**api_timesheets_id_stop_patch**](DefaultApi.md#api_timesheets_id_stop_patch) | **PATCH** /api/timesheets/{id}/stop | Stops an active timesheet record
[**api_timesheets_post**](DefaultApi.md#api_timesheets_post) | **POST** /api/timesheets | Creates a new timesheet record
[**api_timesheets_recent_get**](DefaultApi.md#api_timesheets_recent_get) | **GET** /api/timesheets/recent | Returns the collection of recent user activities
[**api_users_get**](DefaultApi.md#api_users_get) | **GET** /api/users | Returns the collection of all registered users
[**api_users_id_get**](DefaultApi.md#api_users_id_get) | **GET** /api/users/{id} | Return one user entity
[**api_users_id_patch**](DefaultApi.md#api_users_id_patch) | **PATCH** /api/users/{id} | Update an existing user
[**api_users_me_get**](DefaultApi.md#api_users_me_get) | **GET** /api/users/me | Return the current user entity
[**api_users_post**](DefaultApi.md#api_users_post) | **POST** /api/users | Creates a new user
[**api_version_get**](DefaultApi.md#api_version_get) | **GET** /api/version | Returns information about the Kimai release


# **api_activities_get**
> list[ActivityCollection] api_activities_get(project=project, visible=visible, globals=globals, globals_first=globals_first, order_by=order_by, order=order, term=term)

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project = 'project_example' # str | Project ID to filter activities. If none is provided, all activities will be returned. (optional)
visible = 'visible_example' # str | Visibility status to filter activities. Allowed values: 1=visible, 2=hidden, 3=all (default: 1) (optional)
globals = 'globals_example' # str | Use if you want to fetch only global activities. Allowed values: true (default: false) (optional)
globals_first = 'globals_first_example' # str | Deprecated parameter, value is not used any more (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, name, project (default: name) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: ASC) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns a collection of activities
    api_response = api_instance.api_activities_get(project=project, visible=visible, globals=globals, globals_first=globals_first, order_by=order_by, order=order, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_activities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Project ID to filter activities. If none is provided, all activities will be returned. | [optional] 
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Activity ID to fetch

try:
    # Returns one activity
    api_response = api_instance.api_activities_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_activities_id_get: %s\n" % e)
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

Sets the value of a meta-field for an existing activity.

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Activity record ID to set the meta-field value for
body = swagger_client.Body() # Body |  (optional)

try:
    # Sets the value of a meta-field for an existing activity.
    api_response = api_instance.api_activities_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_activities_id_meta_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.ActivityEditForm() # ActivityEditForm | 
id = 56 # int | Activity ID to update

try:
    # Update an existing activity
    api_response = api_instance.api_activities_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_activities_id_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.ActivityEditForm() # ActivityEditForm | 

try:
    # Creates a new activity
    api_response = api_instance.api_activities_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_activities_post: %s\n" % e)
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

# **api_config_i18n_get**
> I18nConfig api_config_i18n_get()

Returns the user specific locale configuration

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns the user specific locale configuration
    api_response = api_instance.api_config_i18n_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_config_i18n_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**I18nConfig**](I18nConfig.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_config_timesheet_get**
> TimesheetConfig api_config_timesheet_get()

Returns the instance specific timesheet configuration

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns the instance specific timesheet configuration
    api_response = api_instance.api_config_timesheet_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_config_timesheet_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TimesheetConfig**](TimesheetConfig.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customers_get**
> list[CustomerCollection] api_customers_get(visible=visible, order=order, order_by=order_by, term=term)

Returns a collection of customers

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
visible = 'visible_example' # str | Visibility status to filter activities (1=visible, 2=hidden, 3=both) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: ASC) (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, name (default: name) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns a collection of customers
    api_response = api_instance.api_customers_get(visible=visible, order=order, order_by=order_by, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_customers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visible** | **str**| Visibility status to filter activities (1&#x3D;visible, 2&#x3D;hidden, 3&#x3D;both) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: ASC) | [optional] 
 **order_by** | **str**| The field by which results will be ordered. Allowed values: id, name (default: name) | [optional] 
 **term** | **str**| Free search term | [optional] 

### Return type

[**list[CustomerCollection]**](CustomerCollection.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customers_id_get**
> CustomerEntity api_customers_id_get(id)

Returns one customer

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns one customer
    api_response = api_instance.api_customers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_customers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CustomerEntity**](CustomerEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customers_id_meta_patch**
> CustomerEntity api_customers_id_meta_patch(id, body=body)

Sets the value of a meta-field for an existing customer.

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Customer record ID to set the meta-field value for
body = swagger_client.Body1() # Body1 |  (optional)

try:
    # Sets the value of a meta-field for an existing customer.
    api_response = api_instance.api_customers_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_customers_id_meta_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Customer record ID to set the meta-field value for | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**CustomerEntity**](CustomerEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customers_id_patch**
> CustomerEntity api_customers_id_patch(body, id)

Update an existing customer

Update an existing customer, you can pass all or just a subset of all attributes

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerEditForm() # CustomerEditForm | 
id = 56 # int | Customer ID to update

try:
    # Update an existing customer
    api_response = api_instance.api_customers_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_customers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerEditForm**](CustomerEditForm.md)|  | 
 **id** | **int**| Customer ID to update | 

### Return type

[**CustomerEntity**](CustomerEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customers_post**
> CustomerEntity api_customers_post(body)

Creates a new customer

Creates a new customer and returns it afterwards

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerEditForm() # CustomerEditForm | 

try:
    # Creates a new customer
    api_response = api_instance.api_customers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_customers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerEditForm**](CustomerEditForm.md)|  | 

### Return type

[**CustomerEntity**](CustomerEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ping_get**
> api_ping_get()

A testing route for the API

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # A testing route for the API
    api_instance.api_ping_get()
except ApiException as e:
    print("Exception when calling DefaultApi->api_ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_projects_get**
> list[ProjectCollection] api_projects_get(customer=customer, visible=visible, start=start, end=end, ignore_dates=ignore_dates, order=order, order_by=order_by, term=term)

Returns a collection of projects.

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
customer = 'customer_example' # str | Customer ID to filter projects (optional)
visible = 'visible_example' # str | Visibility status to filter projects. Allowed values: 1=visible, 2=hidden, 3=both (default; 1) (optional)
start = 'start_example' # str | Only projects that started before this date will be included. Allowed format: HTML5 (default: now, if end is also empty) (optional)
end = 'end_example' # str | Only projects that ended after this date will be included. Allowed format: HTML5 (default: now, if start is also empty) (optional)
ignore_dates = 'ignore_dates_example' # str | If set, start and end are completely ignored. Allowed values: 1 (default: off) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: ASC) (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, name, customer (default: name) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns a collection of projects.
    api_response = api_instance.api_projects_get(customer=customer, visible=visible, start=start, end=end, ignore_dates=ignore_dates, order=order, order_by=order_by, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | **str**| Customer ID to filter projects | [optional] 
 **visible** | **str**| Visibility status to filter projects. Allowed values: 1&#x3D;visible, 2&#x3D;hidden, 3&#x3D;both (default; 1) | [optional] 
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns one project
    api_response = api_instance.api_projects_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_projects_id_get: %s\n" % e)
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

Sets the value of a meta-field for an existing project.

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Project record ID to set the meta-field value for
body = swagger_client.Body2() # Body2 |  (optional)

try:
    # Sets the value of a meta-field for an existing project.
    api_response = api_instance.api_projects_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_projects_id_meta_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectEditForm() # ProjectEditForm | 
id = 56 # int | Project ID to update

try:
    # Update an existing project
    api_response = api_instance.api_projects_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_projects_id_patch: %s\n" % e)
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

# **api_projects_post**
> ProjectEntity api_projects_post(body)

Creates a new project

Creates a new project and returns it afterwards

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectEditForm() # ProjectEditForm | 

try:
    # Creates a new project
    api_response = api_instance.api_projects_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_projects_post: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Search term to filter tag list (optional)

try:
    # Fetch all existing tags
    api_response = api_instance.api_tags_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_tags_get: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Tag ID to delete

try:
    # Delete a tag
    api_instance.api_tags_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->api_tags_id_delete: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TagEditForm() # TagEditForm | 

try:
    # Creates a new tag
    api_response = api_instance.api_tags_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_tags_post: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Fetch all existing teams
    api_response = api_instance.api_teams_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_get: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team whose permission will be revoked
customer_id = 56 # int | The customer to remove (Customer ID)

try:
    # Revokes access for a customer from a team
    api_response = api_instance.api_teams_id_customers_customer_id_delete(id, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_customers_customer_id_delete: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team that is granted access
customer_id = 56 # int | The customer to grant acecess to (Customer ID)

try:
    # Grant the team access to a customer
    api_response = api_instance.api_teams_id_customers_customer_id_post(id, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_customers_customer_id_post: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Team ID to delete

try:
    # Delete a team
    api_instance.api_teams_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_delete: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns one team
    api_response = api_instance.api_teams_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_get: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team from which the member will be removed
user_id = 56 # int | The team member to remove (User ID)

try:
    # Removes a member from the team
    api_response = api_instance.api_teams_id_members_user_id_delete(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_members_user_id_delete: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team which will receive the new member
user_id = 56 # int | The team member to add (User ID)

try:
    # Add a new member to a team
    api_response = api_instance.api_teams_id_members_user_id_post(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_members_user_id_post: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TeamEditForm() # TeamEditForm | 
id = 56 # int | Team ID to update

try:
    # Update an existing team
    api_response = api_instance.api_teams_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team whose permission will be revoked
project_id = 56 # int | The project to remove (Project ID)

try:
    # Revokes access for a project from a team
    api_response = api_instance.api_teams_id_projects_project_id_delete(id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_projects_project_id_delete: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | The team that is granted access
project_id = 56 # int | The project to grant acecess to (Project ID)

try:
    # Grant the team access to a project
    api_response = api_instance.api_teams_id_projects_project_id_post(id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_id_projects_project_id_post: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TeamEditForm() # TeamEditForm | 

try:
    # Creates a new team
    api_response = api_instance.api_teams_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_teams_post: %s\n" % e)
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

# **api_timesheets_active_get**
> list[TimesheetSubCollection] api_timesheets_active_get()

Returns the collection of active timesheet records

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns the collection of active timesheet records
    api_response = api_instance.api_timesheets_active_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_active_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TimesheetSubCollection]**](TimesheetSubCollection.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_timesheets_get**
> list[TimesheetCollection] api_timesheets_get(user=user, customer=customer, project=project, activity=activity, page=page, size=size, tags=tags, order_by=order_by, order=order, begin=begin, end=end, exported=exported, active=active, full=full, term=term)

Returns a collection of timesheet records

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | User ID to filter timesheets. Needs permission 'view_other_timesheet', pass 'all' to fetch data for all user (default: current user) (optional)
customer = 'customer_example' # str | Customer ID to filter timesheets (optional)
project = 'project_example' # str | Project ID to filter timesheets (optional)
activity = 'activity_example' # str | Activity ID to filter timesheets (optional)
page = 'page_example' # str | The page to display, renders a 404 if not found (default: 1) (optional)
size = 'size_example' # str | The amount of entries for each page (default: 50) (optional)
tags = 'tags_example' # str | The name of tags which are in the datasets (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, begin, end, rate (default: begin) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: DESC) (optional)
begin = 'begin_example' # str | Only records after this date will be included (format: HTML5) (optional)
end = 'end_example' # str | Only records before this date will be included (format: HTML5) (optional)
exported = 'exported_example' # str | Use this flag if you want to filter for export state. Allowed values: 0=not exported, 1=exported (default: all) (optional)
active = 'active_example' # str | Filter for running/active records. Allowed values: 0=stopped, 1=active (default: all) (optional)
full = 'full_example' # str | Allows to fetch fully serialized objects including subresources (TimesheetSubCollection). Allowed values: true (default: false) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns a collection of timesheet records
    api_response = api_instance.api_timesheets_get(user=user, customer=customer, project=project, activity=activity, page=page, size=size, tags=tags, order_by=order_by, order=order, begin=begin, end=end, exported=exported, active=active, full=full, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User ID to filter timesheets. Needs permission &#39;view_other_timesheet&#39;, pass &#39;all&#39; to fetch data for all user (default: current user) | [optional] 
 **customer** | **str**| Customer ID to filter timesheets | [optional] 
 **project** | **str**| Project ID to filter timesheets | [optional] 
 **activity** | **str**| Activity ID to filter timesheets | [optional] 
 **page** | **str**| The page to display, renders a 404 if not found (default: 1) | [optional] 
 **size** | **str**| The amount of entries for each page (default: 50) | [optional] 
 **tags** | **str**| The name of tags which are in the datasets | [optional] 
 **order_by** | **str**| The field by which results will be ordered. Allowed values: id, begin, end, rate (default: begin) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: DESC) | [optional] 
 **begin** | **str**| Only records after this date will be included (format: HTML5) | [optional] 
 **end** | **str**| Only records before this date will be included (format: HTML5) | [optional] 
 **exported** | **str**| Use this flag if you want to filter for export state. Allowed values: 0&#x3D;not exported, 1&#x3D;exported (default: all) | [optional] 
 **active** | **str**| Filter for running/active records. Allowed values: 0&#x3D;stopped, 1&#x3D;active (default: all) | [optional] 
 **full** | **str**| Allows to fetch fully serialized objects including subresources (TimesheetSubCollection). Allowed values: true (default: false) | [optional] 
 **term** | **str**| Free search term | [optional] 

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Timesheet record ID to delete

try:
    # Delete an existing timesheet record
    api_instance.api_timesheets_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_id_delete: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Timesheet record ID to duplicate

try:
    # Duplicates an existing timesheet record
    api_response = api_instance.api_timesheets_id_duplicate_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_id_duplicate_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Timesheet record ID to switch export state

try:
    # Switch the export state of a timesheet record to (un-)lock it
    api_response = api_instance.api_timesheets_id_export_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_id_export_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Timesheet record ID to fetch

try:
    # Returns one timesheet record
    api_response = api_instance.api_timesheets_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_id_get: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Timesheet record ID to set the meta-field value for
body = swagger_client.Body4() # Body4 |  (optional)

try:
    # Sets the value of a meta-field for an existing timesheet.
    api_response = api_instance.api_timesheets_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_id_meta_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TimesheetEditForm() # TimesheetEditForm | 
id = 56 # int | Timesheet record ID to update

try:
    # Update an existing timesheet record
    api_response = api_instance.api_timesheets_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_id_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Timesheet record ID to restart
body = swagger_client.Body3() # Body3 |  (optional)

try:
    # Restarts a previously stopped timesheet record for the current user
    api_response = api_instance.api_timesheets_id_restart_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_id_restart_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | Timesheet record ID to stop

try:
    # Stops an active timesheet record
    api_response = api_instance.api_timesheets_id_stop_patch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_id_stop_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TimesheetEditForm() # TimesheetEditForm | 

try:
    # Creates a new timesheet record
    api_response = api_instance.api_timesheets_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_post: %s\n" % e)
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
> list[TimesheetSubCollection] api_timesheets_recent_get(user=user, begin=begin, size=size)

Returns the collection of recent user activities

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | User ID to filter timesheets. Needs permission 'view_other_timesheet', pass 'all' to fetch data for all user (default: current user) (optional)
begin = 'begin_example' # str | Only records after this date will be included. Default: today - 1 year (format: HTML5) (optional)
size = 'size_example' # str | The amount of entries (default: 10) (optional)

try:
    # Returns the collection of recent user activities
    api_response = api_instance.api_timesheets_recent_get(user=user, begin=begin, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_timesheets_recent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| User ID to filter timesheets. Needs permission &#39;view_other_timesheet&#39;, pass &#39;all&#39; to fetch data for all user (default: current user) | [optional] 
 **begin** | **str**| Only records after this date will be included. Default: today - 1 year (format: HTML5) | [optional] 
 **size** | **str**| The amount of entries (default: 10) | [optional] 

### Return type

[**list[TimesheetSubCollection]**](TimesheetSubCollection.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
visible = 'visible_example' # str | Visibility status to filter users. Allowed values: 1=visible, 2=hidden, 3=all (default: 1) (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, username, alias, email (default: username) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: ASC) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns the collection of all registered users
    api_response = api_instance.api_users_get(visible=visible, order_by=order_by, order=order, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_users_get: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 56 # int | User ID to fetch

try:
    # Return one user entity
    api_response = api_instance.api_users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_users_id_get: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserEditForm() # UserEditForm | 
id = 56 # int | User ID to update

try:
    # Update an existing user
    api_response = api_instance.api_users_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_users_id_patch: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Return the current user entity
    api_response = api_instance.api_users_me_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_users_me_get: %s\n" % e)
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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCreateForm() # UserCreateForm | 

try:
    # Creates a new user
    api_response = api_instance.api_users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_users_post: %s\n" % e)
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

# **api_version_get**
> Version api_version_get()

Returns information about the Kimai release

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Returns information about the Kimai release
    api_response = api_instance.api_version_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_version_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

