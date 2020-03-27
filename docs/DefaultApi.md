# swagger_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_config_i18n_get**](DefaultApi.md#api_config_i18n_get) | **GET** /api/config/i18n | Returns the user specific locale configuration
[**api_config_timesheet_get**](DefaultApi.md#api_config_timesheet_get) | **GET** /api/config/timesheet | Returns the instance specific timesheet configuration
[**api_ping_get**](DefaultApi.md#api_ping_get) | **GET** /api/ping | A testing route for the API
[**api_version_get**](DefaultApi.md#api_version_get) | **GET** /api/version | Returns information about the Kimai release


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

