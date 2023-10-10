fw=open("C:\\Users\\shibi\\Desktop\\py_lum\\fileoperations\\years.txt","w")
# write 1800-2024 t0 a File

for y in range(1800,2025):
    fw.write(str(y)+"\n")

fw.close()