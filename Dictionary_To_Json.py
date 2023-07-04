import json
dict = { 'Name' : 'Radhey', 'Age' : '24' }
json_object = json.dumps(dict, indent = 1)
print(json_object)