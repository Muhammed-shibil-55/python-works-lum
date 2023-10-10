# not suppoerted  in python
# instead we use *args or **kwargs method


class calculater:
    def add (self,n1,n2):
        print(n1+n2)

    def add(self,n1,n2,n3):
        print(n1+n2+n3)

obj=calculater()
obj.add(1,2)