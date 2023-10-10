# if row==6 or row+col==7 or col-row==5

for row in range(1,7):
    for sp in range(7-row):
        print(" ", end="") 
    for cols in range(row):
        if row==6 or row+cols==7 or cols-row==5:
            print("* ",end="")
        else:
            print(" ", end="")
    print()