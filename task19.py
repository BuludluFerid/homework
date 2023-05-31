import json

data = '''[
    {"device": "iphone", "price": 3000, "count": null}, 
    {"device": "samsung", "price": 2500, "count": 3},
    {"device": "xiaomi", "price": 2100, "count": null},
    {"device": "nokia", "price": 1800, "count": 4}

]'''

python_data = json.loads(data)
total_price = 0

for item in python_data:
    if item["count"] is not None:
        total_price += item["price"] * item["count"]

print(total_price)
