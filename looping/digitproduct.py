num=int(input("enter the number : "))
product=1
while(num!=0):
    product=product*(num%10)
    num=num//10
print(f"product of the numbers = {product}")