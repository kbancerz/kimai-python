# swagger_client.CustomerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_customers_get**](CustomerApi.md#api_customers_get) | **GET** /api/customers | Returns a collection of customers
[**api_customers_id_get**](CustomerApi.md#api_customers_id_get) | **GET** /api/customers/{id} | Returns one customer
[**api_customers_id_meta_patch**](CustomerApi.md#api_customers_id_meta_patch) | **PATCH** /api/customers/{id}/meta | Sets the value of a meta-field for an existing customer
[**api_customers_id_patch**](CustomerApi.md#api_customers_id_patch) | **PATCH** /api/customers/{id} | Update an existing customer
[**api_customers_id_rates_get**](CustomerApi.md#api_customers_id_rates_get) | **GET** /api/customers/{id}/rates | Returns a collection of all rates for one customer
[**api_customers_id_rates_post**](CustomerApi.md#api_customers_id_rates_post) | **POST** /api/customers/{id}/rates | Adds a new rate to a customer
[**api_customers_id_rates_rate_id_delete**](CustomerApi.md#api_customers_id_rates_rate_id_delete) | **DELETE** /api/customers/{id}/rates/{rateId} | Deletes one rate for an customer
[**api_customers_post**](CustomerApi.md#api_customers_post) | **POST** /api/customers | Creates a new customer


# **api_customers_get**
> list[CustomerEntity] api_customers_get(visible=visible, order=order, order_by=order_by, term=term)

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
visible = 'visible_example' # str | Visibility status to filter activities (1=visible, 2=hidden, 3=both) (optional)
order = 'order_example' # str | The result order. Allowed values: ASC, DESC (default: ASC) (optional)
order_by = 'order_by_example' # str | The field by which results will be ordered. Allowed values: id, name (default: name) (optional)
term = 'term_example' # str | Free search term (optional)

try:
    # Returns a collection of customers
    api_response = api_instance.api_customers_get(visible=visible, order=order, order_by=order_by, term=term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->api_customers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visible** | **str**| Visibility status to filter activities (1&#x3D;visible, 2&#x3D;hidden, 3&#x3D;both) | [optional] 
 **order** | **str**| The result order. Allowed values: ASC, DESC (default: ASC) | [optional] 
 **order_by** | **str**| The field by which results will be ordered. Allowed values: id, name (default: name) | [optional] 
 **term** | **str**| Free search term | [optional] 

### Return type

[**list[CustomerEntity]**](CustomerEntity.md)

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns one customer
    api_response = api_instance.api_customers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->api_customers_id_get: %s\n" % e)
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

Sets the value of a meta-field for an existing customer

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
id = 56 # int | Customer record ID to set the meta-field value for
body = swagger_client.Body1() # Body1 |  (optional)

try:
    # Sets the value of a meta-field for an existing customer
    api_response = api_instance.api_customers_id_meta_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->api_customers_id_meta_patch: %s\n" % e)
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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerEditForm() # CustomerEditForm | 
id = 56 # int | Customer ID to update

try:
    # Update an existing customer
    api_response = api_instance.api_customers_id_patch(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->api_customers_id_patch: %s\n" % e)
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

# **api_customers_id_rates_get**
> list[CustomerRate] api_customers_id_rates_get(id)

Returns a collection of all rates for one customer

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
id = 56 # int | The customer whose rates will be returned

try:
    # Returns a collection of all rates for one customer
    api_response = api_instance.api_customers_id_rates_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->api_customers_id_rates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The customer whose rates will be returned | 

### Return type

[**list[CustomerRate]**](CustomerRate.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customers_id_rates_post**
> CustomerRate api_customers_id_rates_post(id, body)

Adds a new rate to a customer

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
id = 56 # int | The customer to add the rate for
body = swagger_client.CustomerRateForm() # CustomerRateForm | 

try:
    # Adds a new rate to a customer
    api_response = api_instance.api_customers_id_rates_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->api_customers_id_rates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The customer to add the rate for | 
 **body** | [**CustomerRateForm**](CustomerRateForm.md)|  | 

### Return type

[**CustomerRate**](CustomerRate.md)

### Authorization

[apiToken](../README.md#apiToken), [apiUser](../README.md#apiUser)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customers_id_rates_rate_id_delete**
> api_customers_id_rates_rate_id_delete(id, rate_id)

Deletes one rate for an customer

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
id = 56 # int | The customer whose rate will be removed
rate_id = 56 # int | The rate to remove

try:
    # Deletes one rate for an customer
    api_instance.api_customers_id_rates_rate_id_delete(id, rate_id)
except ApiException as e:
    print("Exception when calling CustomerApi->api_customers_id_rates_rate_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The customer whose rate will be removed | 
 **rate_id** | **int**| The rate to remove | 

### Return type

void (empty response body)

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerEditForm() # CustomerEditForm | 

try:
    # Creates a new customer
    api_response = api_instance.api_customers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->api_customers_post: %s\n" % e)
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

