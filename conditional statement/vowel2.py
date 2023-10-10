word=input("enter a word").casefold()
if(word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u"):
    print("vowel")
else:
    print("consonant")