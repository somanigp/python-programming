import requests
import datetime as dt

PIXELA_URL = "https://pixe.la"
USERNAME = "somanigp"
PIXELA_API_TOKEN = "loykszJOD0ByDdAdPA8"

# These are two different ways of sending data to the server:

# 1. **Params** (short for parameters) are typically used with **GET** requests and are appended to the request URL.
# They are visible in the URL and are used to send simple, less sensitive data. For example, if you're requesting a
# specific user's data, you might include the user's ID as a parameter. Parameters provide data to the server. They can
# be used to filter, sort, or pass data to the server in a GET request. Best practice is to have token in headers
#
# 2. The **body** of an API request is used to send the actual request data. This is typically used with **POST** and
# **PUT** requests, which are designed to create or update resources on the server. The body can contain more complex
# data structures, like JSON or XML, and is not visible in the URL. This makes it a good choice for sending sensitive
# or large amounts of data. The body carries the actual data sent to the server, typically used in POST, PUT, DELETE,
# and PATCH requests. This data might include form data, JSON, XML, or other data formats.
#
# In summary, params are used for simple, less sensitive data and are visible in the URL, while the body is used for
# more complex or sensitive data and is not visible in the URL.

# 3. Headers provide metadata about the request or response. They convey information such as the type of data
# being sent, the encoding, and instructions for caching, among other things. Ex: Content-Type: application/json,
# Authorization (So the key is not visible to others)

# NOTE: There are different ways to send tokens which are mentioned in API docs. - So read those.

# 4 common types of http(Hypertext Transfer Protocol) req: get, post (giving/sending data and not bothering about
#  response), put (update a piece of data in external service) and delete (delete the data in external service).

# Creating a User
# data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
# json – (optional) A JSON serializable Python object to send in the body of the Request.
# NOTE: json is just for json type, but we can put that in data also, data can have json, xml, etc.

# create_user_url = PIXELA_URL + "/v1/users"  # Separate main url and api url
# json_body = {   # Body to send, see docs for requirements
#     "token": "loykszJOD0ByDdAdPA8",
#     "username": "somanigp",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=create_user_url, json=json_body)
# response.raise_for_status()
# print(response.text)  # response as text

# Create Graph Definition
# create_graph_url = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs"  # Way to create url
# headers = {  # Passing Auth Key in headers
#     "X-USER-TOKEN": PIXELA_API_TOKEN
# }
# request_body = {
#     "id": "graph1",
#     "name": "Mobile Use Tracker",
#     "unit": "hours",
#     "type": "float",
#     "color": "shibafu",
#     "timezone": "Asia/Calcutta"
# }
# response = requests.post(url=create_graph_url, json=request_body, headers=headers)
# response.raise_for_status()
# print(response.text)

# Add a Pixel
current_date = dt.datetime.now()
# String-of-time method: https://www.w3schools.com/python/python_datetime.asp
# print(current_date.strftime("%Y%m%d"))  # Format using strftime(). O/P is str. y - 24, Y - 2024, etc. See docs.
current_date_in_strings = current_date.strftime("%Y%m%d")
pixel_post_url = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/graph1"
headers = {
    "X-USER-TOKEN": PIXELA_API_TOKEN
}
request_body = {  # We are sending a json data and thus use json in req.post method.
    "date": current_date.strftime("%Y%m%d"),  # Current date
    "quantity": input("how many hours spent on mobile/tablet today???")
}
response = requests.post(url=pixel_post_url, json=request_body, headers=headers)
response.raise_for_status()
print(response.text)


# Update a pixel: PUT
pixel_update_url = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/graph1/{current_date_in_strings}"
request_body_for_update = {
    "quantity": "6"
}
# response = requests.put(url=pixel_update_url, headers=headers, json=request_body_for_update)
# response.raise_for_status()
# print(response.text)

# Delete a pixel:
# delete_pixel_url = f"{PIXELA_URL}/v1/users/{USERNAME}/graphs/graph1/{current_date.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixel_url, headers=headers)
# response.raise_for_status()
# print(response.text)

# NOTES:
# Difference between json and data:
# The json and data arguments are used to send data in different formats.

# 1. json: This argument is used to send JSON data in the body of the POST request.When you pass a Python dictionary to
# the json argument, requests automatically serializes it to a JSON string and sets the Content-Type
# header to application/json. json sets the Content-Type header to application/json automatically.
# data does not set the Content-Type header automatically unless you provide form-encoded data.

# 2. data: This argument is used to send form-encoded data or raw data in the body of the POST request.When you pass
# a dictionary to the data argument, requests encodes it as application/x-www-form-urlencoded (form data).
# If you pass a string, it sends the string as raw data.json automatically serializes a Python dictionary
# to a JSON string.
# data encodes a Python dictionary to form-encoded data (application/x-www-form-urlencoded) or sends raw data if a
# string is provided.

# url = 'https://example.com/api/resource'
# payload = {  # Form-encoded data
#     'key1': 'value1',
#     'key2': 'value2'
# }
#
# response = requests.post(url, data=payload)

# raw_data = 'key1=value1&key2=value2'  # Raw data
# response = requests.post(url, data=raw_data)

# NOTE: *** All depends on what kind of data the server is expecting.
# NOTE: Use the json argument when you need to send JSON data to an API endpoint that expects JSON.
# Use the data argument when you need to send form-encoded data (like submitting a form) or raw data
# to an endpoint that expects such formats.
# choose json when interacting with APIs that expect JSON payloads and data for form submissions
# or when sending raw data.
