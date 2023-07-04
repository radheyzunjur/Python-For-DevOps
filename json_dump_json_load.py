import json

data = {"name": "John", "age": 30, "city": "New York"}

with open("services.json", "w") as file:
    json.dump(data, file)

print(data)