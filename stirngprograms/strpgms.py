name="SOOrajnS10"
print(name.casefold()) # convert all characters to lower case
print(name.capitalize()) # convert first letter of the word into upper case
print(name.count("O")) # find count of a specific letter in the string
print(name.index("a")) # return the first occurence position of the letter in the str
print(name.strip("S")) # remove the given letter from right or left or both but not in between
print(name.rstrip("S")) # remove the given letter from right 
print(name.lstrip("S")) # remove the given letter from left 
print(name.isalpha())  # confirm the given str has alphabets only
print(name.isdigit()) # confirm the given str has digit only
print(name.isalnum()) ## confirm the given str has digit and alphabts  only
print(name.startswith("S")) # check the first letter 
print(name.endswith("s")) #check the last letter
stri="python is a programming language"
words=stri.split(" ")
print(words)

for w in words:
    print(w)

# print words starting with vowels