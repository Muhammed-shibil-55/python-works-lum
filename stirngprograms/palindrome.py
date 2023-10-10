text="malayalam"
#q2 check whether kangaroo word
# kangaroo word > text=chicken
#                  out=> hen
out=""
for t in range(len(text)-1,-1,-1):
    out=out+text[t]
print(out)
if(out==text):
    print("palindrome")
else:
    print("nope")