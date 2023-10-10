n1=int(input("enter the number 1:"))
n2=int(input("enter the number 2:"))

sub=n1-n2 if n1>n2 else n2-n1 if n2>n1 else "equal"
print(sub)