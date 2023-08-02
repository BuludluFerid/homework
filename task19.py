# import json

# data = '''[
#     {"device": "iphone", "price": 3000, "count": null}, 
#     {"device": "samsung", "price": 2500, "count": 3},
#     {"device": "xiaomi", "price": 2100, "count": null},
#     {"device": "nokia", "price": 1800, "count": 4}

# ]'''

# python_data = json.loads(data)
# total_price = 0

# for item in python_data:
#     if item["count"] is not None:
#         total_price += item["price"] * item["count"]

# print(total_price)



'''İçində olduğunuz dirin parentinin parentində olan faylların extensionlarını göstərən program hazırlayın.'''

# from pathlib import Path
# current_path = Path('.').absolute()
# parent = current_path.parent.parent
# data = list(parent.iterdir())
# extensions = []
# for i in data:
#     if i.is_file():
#         extensions.append(i.suffix)
# print(extensions)


# import json
# from uuid import uuid4
# import secrets

# with open('info.json', mode="r") as file:
#     data = json.load(file)

# for datas in data:
#     datas['ID'] = str(uuid4())
#     datas['Password'] = secrets.token_urlsafe(10)

# with open('info.json', mode="w") as new_file:
#     json.dump(data, new_file, indent=4)


