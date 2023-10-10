mrk=int(input("enter your mark :"))
if(mrk>100):
    print("INVALID MARK")
elif(mrk>=90):
    print("you scored A+")
elif(mrk>=80):
    print("you scored A")
elif(mrk>=70):
    print("you scored B+")
elif(mrk>=60):
    print("you scored B")
elif(mrk>=50):
    print("you scored C+")
elif(mrk>=40):
    print("you scored C")
elif(mrk>=30):
    print("you scored D+")
else:
    print("sorry you have failed")        