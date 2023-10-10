# class Person:
#     def __init__(self):
#         self.name="subash"
#     def bio(self):
#         self.adr="abc"
#         self.course="xyz"
# obj=person()
# print(obj.name)

# class Student:
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course
#     def get_student(self):
#         print("my name is",self.name,"my course is",self.course)

# obj=Student("shibil","django")
# obj.get_student()
# obj1=Student("sooraj","mearn")
# obj1.get_student()

# class Book:
#     def __init__(self) -> None:
#         self.id=int(input("enter your id"))
#         self.title=input("enter title")
#         self.author=input("enter name of author")
#         self.price=int(input("enter price"))
#     def get_author(self):
#         print(self.author)
#     def get_title(self):
#         print(self.title)
#     def setprice(self):
#         self.price=int(input("enter price"))
#     def settitle(self):
#         self.title=input("enter title")
#     def getdetails(self):
#         print(self.id)
#         print(self.title)
#         print(self.author)
#         print(self.price)
# b1=Book()
# b1.get_author()
# b1.get_title()
# b1.setprice()
# b1.settitle()
# b1.getdetails()


# inheritance
class Things:
    def mobile(self):
        print("vivo")
    def bike(self):
        print("pulsar")
    def car(self):
        print("dodge")

class Child(Things):
    pass

c1=Child()
c1.bike()
c1.car()
c1.mobile()