mrk=int(input("enter your mark :"))
if(mrk>100):
    print("INVALID MARK")
if(mrk>=90 and mrk<100):
    print("you scored A+")
if(mrk>=80 and mrk<90):
    print("you scored A")
if(mrk>=70 and mrk<80):
    print("you scored B+")
if(mrk>=60 and mrk<70):
    print("you scored B")
if(mrk>=50 and mrk<60):
    print("you scored C+")
if(mrk>=40 and mrk<50):
    print("you scored C")
if(mrk>=30 and mrk<40):
    print("you scored D+")
if(mrk<30):
    print("sorry you have failed")   