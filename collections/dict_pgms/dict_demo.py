mobile={"name":"v25","brand":"vivo","price":28000,"color":"green"}
print(mobile["name"])

# adding new key value pair
# display:amoled
# dict_obj[key]=value
mobile["display"]="amoled"
print(mobile)

# checking whether a key is in the dictionary or not

if "offer" in mobile:
    print("offer key is present")
else:
    print("not exist")