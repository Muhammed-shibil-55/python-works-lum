items=[
    {"id":1,"name":"v25","brand":"vivo","price":28000},
    {"id":2,"name":"a25","brand":"samsung","price":25000},
    {"id":3,"name":"s23","brand":"samsung","price":100000},
    {"id":4,"name":"y5","brand":"huawei","price":8000},
    {"id":5,"name":"13","brand":"iphone","price":45000}

]

def add_item(*args,**kwargs):
    items.append(kwargs)

add_item(id=6,name="9a",brand="redmi",price=10000)
print(items)

def retrive_item(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id]
    return obj

print(retrive_item(id=1))

def update_item(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id][0]
    obj.update(kwargs)

update_item(id=3,name="s23 ultra",price=150000)
print(items)

def delete_item(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id][0]
    items.remove(obj)

delete_item(id=6)
print(items)