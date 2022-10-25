import json

with open('person.json', 'r+') as f:
  data = json.load(f)

data["newtag"] = "test"

with open('person.json', 'w') as f:
    json.dump(data, f, indent=4)


print(data)
print(json.dumps(data, indent = 4, sort_keys=True))