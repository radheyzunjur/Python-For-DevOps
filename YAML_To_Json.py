import yaml
import json

# Read the YAML file
with open('services.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Convert YAML to JSON
json_data = json.dumps(data)

# Print the JSON data
print(json_data)
