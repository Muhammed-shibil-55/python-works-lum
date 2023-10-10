
for row in range(7):
    for sp in range(7-row):
        print(" ", end="") 
    for cols in range(row*2+1):
        if cols==0 or row==6 or cols==row*2:
            print("*",end="")
        else:
            print(" ", end="")
    print()