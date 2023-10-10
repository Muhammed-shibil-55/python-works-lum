class Bank:
    accno:int
    person_name:str
    ifsc_code:int
    branch:str
    acc_type:str
    balance:int
    bank_name:str

    def create(self,accno,name,ifsccode,branch,acc_type,bal,bank_name):
        self.accno=accno
        self.person_name=name
        self.ifsc_code=ifsccode
        self.branch=branch
        self.acc_type=acc_type
        self.balance=bal
        self.bank_name=bank_name
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} account has been credited with amount {amount} aval bal {self.balance}")

    def withdrawal(self,amount):
        if(amount>self.balance):
            print("insufficient balance transaction declined")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} account has been debited with amount {amount} aval bal {self.balance}")
    
    def get_balance(self):
        print(f"your aval bal is {self.balance}")

acc1=Bank()
acc1.create(1123,"sooraj",5599029,"pattambi","minimum balance",2300,"punjab national bank")
acc1.deposit(5000)
acc1.withdrawal(3500)
acc1.get_balance()