st1={10,2,19,20,4}
st2={10,20,30}

# add an element to the set
st1.add(200)
print(st1)

# union of two sets
union_set=st1.union(st2)
print(union_set)

# intersection of two sets
inter_set=st1.intersection(st2)
print(inter_set)

# difference of two sets
differ_set=st1.difference(st2)
print(differ_set)

# remove an element from a set
st1.remove(200)
print(st1)

st1.discard(1000) #deosnot return error while removing element when we give and element not in set
print(st1) 

st1.pop() # remove random object
print(st1)




# symmetric difference
st3={4,5,2,8}
st4={2,8,6,7}
symmdiff_set=st3.symmetric_difference(st4)
print(symmdiff_set)