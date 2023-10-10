class parent:
    phone="vivo v25"
    bike="pulsar 180"

    def mobile(self):
        print(self.phone)
    def vehicle(self):
        print(self.bike)

class child(parent):
    pass

obj=child()
obj.mobile()
obj.vehicle()
