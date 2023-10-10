f=open("C:\\Users\\shibi\\Desktop\\py_lum\\fileoperations\\data.txt","r")

lines=[line.rstrip("\n") for line in f]

print(lines)