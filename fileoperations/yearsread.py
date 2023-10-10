# read from years.txt
# write leapyears to leayear.txt
# write non leapyears to nonleapyear.txt

fr=open("C:\\Users\\shibi\\Desktop\\py_lum\\fileoperations\\years.txt")
lp_yr=open("C:\\Users\\shibi\\Desktop\\py_lum\\fileoperations\\leapyear.txt","w")
nlp_yr=open("C:\\Users\\shibi\\Desktop\\py_lum\\fileoperations\\nonleapyear.txt","w")
for yr in fr:
    y=int(yr)
    if(y%100==0 and y%400==0):
        lp_yr.write(str(y)+"\n")
    elif(y%100!=0 and y%4==0):
        lp_yr.write(str(y)+"\n")
    else:
        nlp_yr.write(str(y)+"\n")

fr.close()
lp_yr.close()
nlp_yr.close()
    

