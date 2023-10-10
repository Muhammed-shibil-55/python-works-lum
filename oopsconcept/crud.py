items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"veg friedrice","price":140},
    {"id":102,"name":"ghee roast","price":70},
    {"id":103,"name":"alfaham","price":460},
    {"id":104,"name":"porrotta","price":10},
    {"id":105,"name":"chicken roast","price":150}
]

def add_item(*args,**kwargs):
    items.append(kwargs)

add_item(id=106,name="bb",price=140)

# print(items)

def retrieve_item(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id]
    return (obj)

# print(retrieve_item(102))

def destroy_item(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id][0]
    items.remove(obj)

# destroy_item(id=103)
# print(items)

def update_items(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id][0]
    obj.update(kwargs)

update_items(id=102,name="masala dosa",price=80)
# print(items)

print(retrieve_item(id=100))


