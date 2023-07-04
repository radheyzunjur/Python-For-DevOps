import json

# Read the JSON file
with open('services.json', 'r') as file:
    data = json.load(file)

# Extract service names for each cloud provider
for provider, services in data.items():
    service_name = services.get('name')
    print(f"{provider} : {service_name}")
