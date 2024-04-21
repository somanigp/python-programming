# requests library in Python for making HTTP requests:
import requests

# Make a GET request:
# Get the response from a URL
response = requests.get('https://api.example.com/data') # This sends a GET request to the specified URL and assigns the response object to the response variable.
# Status code: Check the HTTP status code using response.status_code.
# Get the response content as text using response.text, as JSON using response.json(), or in other formats depending
# on the server's response.
# Headers: Access response headers using response.headers.
response_params = requests.get('https://api.example.com/data', params={'key': 'value'})

if response.status_code == 200:
    # Check content type before accessing directly
    if response.headers['Content-Type'] == 'application/json':
        data = response.json()
    else:
        data = response.text
    print(data)
else:
    print(f"Error: HTTP status code {response.status_code}")

# The requests library supports various HTTP methods besides GET:
#
# POST: Submit data to a server (often for creating or updating resources)
# PUT: Update an existing resource
# DELETE: Delete a resource
# PATCH: Apply partial updates to a resource

# Each method takes similar arguments as GET, with additions like data for POST and PUT:
response_post = requests.post('https://api.example.com/users', data={'name': 'Alice'})
response_put = requests.put('https://api.example.com/articles/123', data={'title': 'New Title'})

# Authentication and Customizations:
#
# Authentication: Use auth arguments like auth=('username', 'password') for basic authentication or refer to requests documentation for other methods.
# Headers: Specify custom headers in the headers parameter, e.g., headers={'Authorization': 'Bearer YOUR_TOKEN'}.
# Timeouts: Set timeouts using timeout to prevent hanging requests (e.g., timeout=5).
# Proxies: Configure proxies with the proxies parameter for routing requests through proxies.

try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    # Process successful response
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")


