# pip install requests
import requests 

# response = requests.get("https://reqres.in//api/users/4")
# print(response)
# print(response.text)

# json_data = response.json()
# print(json_data)

# print(json_data['data']['email'])
# print(json_data['data']['last_name'])

# 200 - 299 ---> Success 
# 300 - 399 ---> Redirection 
# 400 - 499 ---> Client Side error --> 404 - Page Not Found
#  500 -599 --> Server side errors


# -------------------------------------------------------------------
# POST -- HTTP -- To send some data to server

# payload = {"name":"Arvinder","City":"Sirsa"}

# response = requests.post("https://httpbin.org/post",data=payload)
# print(response.text)

# Adding Query Parameters 

payload = {"name":"Skanda","Country":"USA"}

# response = requests.get("https://httpbin.org/get",params=payload)
# print(response.text)

# payload = {'page':2,'per_page':3}
# response = requests.get("https://reqres.in/api/users",params=payload)
# print(response.text)

# header 
# headers = {
#     'my-agent':"HelloSingh",
#     'Code':"in Python"
# }

# response = requests.get("https://httpbin.org/headers",headers=headers)
# print(response.text)

# Error 
# response = requests.get("https://httpbin.org/status/404")
# try:
#   response.raise_for_status()
# except requests.exceptions.HTTPError:
#   print("HTTP error found")


# Delay

# response = requests.get("https://httpbin.org/delay/2",timeout=2)
# print(response.text)

# try:
#   reponse = requests.get("https://arvinderpal.singh.hello.com")
# except requests.exceptions.ConnectionError:
#   print("Connection Error")
