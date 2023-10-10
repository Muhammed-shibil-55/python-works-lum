# variable length argument method

def product(*args): # * -> any number of arguments accept as tuple
    res=1
    for n in args:
        res*=n
    print(res)

product(1,2,3,4)
product(10,20)

def greeting(**kwargs): # **-> any number of arguments accept as dictionary
    print(f"hello {kwargs.get('msg')} app user {kwargs.get('username')}")

greeting(msg="good morning",username="shibil")

def dispatch_order(**kwargs):
    print(f"hello user {kwargs.get('name')} your order {kwargs.get('code')} {kwargs.get('item')} is ready to {kwargs.get('status')}")

dispatch_order(item="ucb shirt",code="123bc",status="deliver",name="sooraj")