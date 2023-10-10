f=open("C:\\Users\\shibi\\Desktop\\py_lum\\fileoperations\\numbers.txt")
all_numbers=[line.rstrip("\n") for line in f]
print(all_numbers)

kerala_numbs=[numb for numb in all_numbers if numb.startswith("kl")]
print(kerala_numbs)