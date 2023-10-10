class Hotel:
    items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"veg friedrice","price":140},
    {"id":102,"name":"ghee roast","price":70},
    {"id":103,"name":"alfaham","price":460},
    {"id":104,"name":"porrotta","price":10},
    {"id":105,"name":"chicken roast","price":150}
    ]

    def create(self,*args,**kwargs):
        self.items.append(kwargs)
        return f"{kwargs} created"
    

    def retrieve(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
        return obj
    
    def destroy(self,id=None,*args,**kwargs):
        obj=[i for i in self.items if i.get("id")==id][0]
        self.items.remove(obj)
        return f"{obj} has been removed"
    
    def update(self,id=None,*args,**kwargs):
        obj=self.retrieve(id=id)
        old_obj=obj.copy()
        obj.update(kwargs)
        return f"{old_obj} has been updated to {obj}"
    

obj=Hotel()
# print(obj.create(id=106,name="noodles",price=80))
# print(obj.retrieve(id=101))
# print(obj.destroy(id=102))
print(obj.update(id=102,name="GHEE ROAST"))
