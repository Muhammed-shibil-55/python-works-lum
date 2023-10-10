class Employee:
    id:int
    name:str
    gender:str
    department:str
    salary:int

    def create(self,id,name,gender,dept,sal):
        self.id=id
        self.name=name
        self.gender=gender
        self.department=dept
        self.salary=sal

    def get(self):
        print(self.id,self.name,self.department,self.salary)

emp1=Employee()
emp1.create(100,"sooraj","male","sales",300000)

emp2=Employee()
emp2.create(101,"shibil","male","hr",450000)

emp1.get()
emp2.get()
