stri=input("enter the string : ").casefold
vowcount=0
conscount=0
def vow(s,v,c):
    for ch in s:
        if ch in ["a","e","i","o","u"]:
            v=v+1
        else:
            c=c+1
    print("number of vowels =",v)
    print("number of consonants =",c)

vow(stri,vowcount,conscount)

# len(str) - used to find the length of string