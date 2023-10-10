# abstraction

from abc import ABC,abstractmethod

class Bike(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelorater(self):
        pass
    @abstractmethod
    def brake(self):
        pass
class Pulsar(Bike):
    def start(self):
        print("pulsar starts")
    def accelorater(self):
        print("pulsar accelorates")
    def brake(self):
        print("pulsar brakes")



obj=Pulsar()
obj.start()
obj.accelorater()
obj.brake()