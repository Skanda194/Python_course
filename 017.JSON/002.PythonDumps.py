import json

x = { "name":"Arvinder",
     "age":30,
     "City":"England"
    }

# It converts the Python code into json
result = json.dumps(x)

print(result)

# Any python object can be converted into json

# dictionary , list , int , float, boolean , tuple , strings

# name = "Python"

# print(json.dumps(name))

