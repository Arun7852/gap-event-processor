import json 

with open('event.json', 'r') as file:
    data = json.load(file)

print(data)
