path="C:\\Users\\shibi\\Desktop\\py_lum\\fileoperations\\test.txt"
f=open(path)
test=[]
for l in f:
    test.append(l.rstrip("\n"))
print(test)
