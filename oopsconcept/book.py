class Book:
    Book_name:str
    Author:str
    Price:int
    pages:int
    
    def __init__(self,name,author,price,pages):
        self.Book_name=name
        self.Author=author
        self.Price=price
        self.pages=pages
    
    def get(self):
        print(self.Book_name,self.Author,self.Price,self.pages)

    def __str__(self):  # string representation of object
        return self.Book_name

bk1=Book("balarama","mathrubhoomi",20,125)
bk1.get()
bk2=Book("aarachar","meera",560,600)
bk2.get()
print(bk1)
print(bk2)