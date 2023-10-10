mobile={"name":"v25","brand":"vivo","price":28000,"color":"green","offer":100}

if "offer" in mobile:
    mobile["offer"]+=50
else:
    mobile["offer"]=50
print(mobile)