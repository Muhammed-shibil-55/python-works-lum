users=["vijay","surya","fahad","karthi","sk","str","vadivelu","sk"]
# add new objects in to the list

users.append("kamal hasan")
print(users)

# remove an object from the list

users.pop(2) # default pop value is -1/last object
print(users) 

# to know the index position of an object

print(users.index("sk"))

# to know the occurence of the objects

print(users.count("sk"))

# sort the list

users.sort()
print(users)

# to remove all the elements from the list

# users.clear()
# print(users)

# check whether an object is in the list or not
if ("rolex" in users):
    print("present")
else:
    print("not present")

if("rolex" not in users):
    users.append("rolex")
print(users)

# remove object

users.remove("rolex")
print(users)