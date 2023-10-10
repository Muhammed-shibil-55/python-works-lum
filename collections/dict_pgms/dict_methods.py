student={"name":"shibil","course":"django","is_placed":True,"salary":100000}

# return all the keys in dictionary
print(student.keys())

for k in student.keys():
    print(k)      # print keys one by one
print("")

# return all the values in dictionary
for v in student.values():
    print(v)
print("")

# return both key and value
for k,v in student.items():
    print(k,":",v)
print("")

# method for fetching value using key
print(student.get("name"))

print("")

# remove key and value pair from dictionary
student.pop("is_placed")
print(student)
print()

#
