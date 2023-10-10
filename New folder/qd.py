class books:
    data=[
        {"id":"100","name":"python","price":"350"},
        {"id":"101","name":"java","price":"450"},
        {"id":"102","name":"django","price":"1300"},
        {"id":"103","name":"html","price":"1000"},
        {"id":"104","name":"bootstrap","price":"300"}
    ]

    
    def items(self):
        for d in self.data:
            print(d)

    def retrieve(self,id):
        self.id=id
        self.lst=[d for d in self.data if d["id"] == id]
        print(self.lst[0])

    def update(self,id=None,*args,**kwargs):
        self.id=id
        self.lst=[d for d in self.data if d.get("id") == id][0]
        self.lst.update(kwargs)
        print("book updated")

    def delete(self,id):
        self.id=id
        self.obj=[d for d in self.data if d.get("id") == id][0]
        self.data.remove(self.obj)
        print("book removed")
        print(self.data)

        
        

book=books()
book.items()
id=input("enter the id of book : ")
book.retrieve(id)
book.update(id="103",price=1200,name="css")
obj=input("enter the id of book to be removed : ")
book.delete(obj)