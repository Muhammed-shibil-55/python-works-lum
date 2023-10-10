# you are havin an arithmetic sequence of difference 6
# starting number is 56 find the sum of 10 terms in the sequence

strt=56
i=1
sum=0
while(i<=10):
    sum=sum+strt
    strt+=6
    i+=1
print("sum of the first ten number in the sequence =",sum)
