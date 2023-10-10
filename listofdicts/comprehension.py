# list comprehension
lst=[1,3,2,4,7,6,5,8]

squares=[l**2 for l in lst ]
print(squares)

cubes=[l**3 for l in lst ]
print(cubes)

evens=[l for l in lst if l%2==0]
print(evens)

odd=[l for l in lst if l%2!=0]
print(odd)

num_gtr5=[l for l in lst if l>5]
print(num_gtr5)

lst2=[l for l in lst]
print(lst2)