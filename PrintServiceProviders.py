import json
with open("services.json") as jsonfile:
  jsonObject=json.load(jsonfile)
  jsonfile.close()
print (jsonObject)
print("aws : ", jsonObject["services"]["aws"]["name"])
print("azure : ", jsonObject["services"]["azure"]["name"])
print("gcp : ", jsonObject["services"]["gcp"]["name"])