# API - Application Programming Interface
# API is a set of rules that allows different software applications to communicate with each other. It
# defines how requests and responses should be formatted, what data can be accessed, and what actions can be performed.
# APIs are used to enable integration between different systems, allowing them to share data and functionality.
# For example, when you use a weather app on your phone, it may use an API
# to fetch weather data from a remote server. The app sends a request to the API, 
# which processes the request and returns the relevant weather information that the app can then display to you.

# API Endpoints are specific URLs that represent different resources or actions within an API. 
# They are the points of interaction where clients can send requests to access or manipulate data. 
# Each endpoint typically corresponds to a specific function or operation that the API provides. 
# For example, in a weather API, there might be an endpoint like "/current-weather" 
# that allows clients to retrieve the current weather information for a given location. 
# Endpoints are essential for defining how clients can interact with the API and what functionality is available.

import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response) # This will print the response object, which contains information about the HTTP response received from the server. 
# #It includes details such as the status code, headers, etc. The status code indicates whether the request was successful 
# # (e.g., 200 for OK) or if there was an error (e.g., 404 for Not Found). 

# # 1XX: Hold open
# # 2XX: Success
# # 3XX: GO Away/Redirection
# # 4XX: You Screwed Up/Client Error
# # 5XX: I screwed Up/Server Error

# print(response.status_code) # This will print the status code of the HTTP response, which indicates the result of the request.

# if response.status_code != 200:
#     raise Exception("Error: API request unsuccessful") # This line raises an exception if the status code is not 200, indicating that the API request was unsuccessful.

# response.raise_for_status() # This line will raise an HTTPError if the HTTP request returned an unsuccessful status code (i.e., not in the 200-299 range).

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

latitude = response.json()["iss_position"]["latitude"] # This line extracts the latitude of the International Space Station (ISS) from the JSON response received from the API.
longitude = response.json()["iss_position"]["longitude"] # This line extracts the longitude of the International Space Station (ISS) from the JSON response received from the API.

iss_position = (latitude, longitude) # This line creates a tuple called iss_position that contains the latitude and longitude of the ISS.

print(iss_position) # This will print the tuple containing the latitude and longitude of the International Space Station (ISS).
