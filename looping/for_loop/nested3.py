for row in range(1,7):
    for sp in range(7-row,1,-1):
        print(" ",end="")
    for col in range(row):
        print("* ",end="")
    print()