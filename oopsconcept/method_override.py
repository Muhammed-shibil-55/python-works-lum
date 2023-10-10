

class Car:
    def start(self):
        print("key start")
    def break_type(self):
        print("drum break")
    def transmission(self):
        print("manual")
class Ambassador(Car):
    pass
class Maruthi800(Car):
    def break_type(self):
        print("disc break")

car1=Ambassador()
car1.start()
car1.break_type()
car1.transmission()

car2=Maruthi800()
car2.start()
car2.break_type()
car2.transmission()