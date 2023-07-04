fav_tools = {
  1: "Linux",
  2: "Git",
  3: "Docker",
  4: "Kubernetes",
  5: "Terraform",
  6: "Ansible",
  7: "Chef"
}

favorite_tool_key = int(input("Enter the key"))

# Printing the favorite tool using its key
if favorite_tool_key in fav_tools:
    a= fav_tools[favorite_tool_key]
    print(f"My favorite tool is {a}")
else:
    print("Tool not found in the dictionary.")
