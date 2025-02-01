# JSON -  

'''
{
    '1':'Skanda',
    '2': 'Arvinder',
    '3': 'Gagan'    
}
'''
# json library 

# import json 

import json
obj = '{ "name":"Arvinder","age":30,"City":"England"}'

# json.loads() --> convert the json object to python dictionary
result = json.loads(obj)

print(result["City"])
