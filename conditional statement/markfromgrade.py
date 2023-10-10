# enter a grade and print category of the mark


grade=input("enter the grade in capital : ")
if(grade=="A+"):
    print("your mark is between 90 and 100 .")
elif(grade=="A"):
    print("your mark is between 80 and 90 .")
elif(grade=="B+"):
    print("your mark is between 70 and 80 .")
elif(grade=="B"):
    print("your mark is between 60 and 70.")
elif(grade=="C+"):
    print("your mark is between 50 and 60 .")
elif(grade=="C"):
    print("your mark is between 40 and 50.")
elif(grade=="D+"):
    print("your mark is between 30 and 40 .")
else:
    print("you have failed..")