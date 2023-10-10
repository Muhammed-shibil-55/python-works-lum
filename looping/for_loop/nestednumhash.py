for row in range(1,7):
    for col in range(1,row+1):
        if(col%2==0):
            print("#",end="\t")
        else:
            print(col,end="\t")
    print()