import json

with open('list.json', 'r') as f:
    list = json.load(f)
print(list)

new_list = []
for li in list:
    new_data = {"model": "pictures.mind"}
    new_data["fields"] = {}
    new_data["fields"]["name"] = li
    new_list.append(new_data)

print(new_list)

with open('list_loader.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)

