from json import load

path="C:\\Users\\shibi\\Desktop\\py_lum\\movies\\mdb.json"
with open(path,encoding="utf-8") as f:
    films=load(f)
# print total number of films
print(len(films))

# print all movies names released in 2015
movie_filter=[f.get("title") for f in films if f.get("year")=="2015"]
# print(movie_filter)

# print all movies whose genre is comedy
funny_movies=[f.get("title") for f in films if "Comedy" in f.get("genres")]
# print(funny_movies)

# id in range(20,30) and runtime > 110

m_filter=[f.get("title") for f in films if f.get("id") in range(20,31) and f.get("runtime")>="110"]
# print(m_filter)

# one worded title
title_filter=[f.get("title") for f in films if len(f.get("title").split(" "))==1]
# print(title_filter)

# highest drama runtime
drama_genre=[f for f in films if "Drama" in f.get("genres")]
drama_max=max(drama_genre,key=lambda d:int(d.get("runtime")))
# print(drama_max)


# print list of all genres
genres=[]
for f in films:
    genre=f.get("genres")
    for g in genre:
        if g not in genres:
            genres.append(g)
print(genres)            

# most movies released year
yeardict={}
for f in films:
    yr=f.get("year")
    if yr in yeardict:
        yeardict[yr]+=1
    else:
        yeardict[yr]=1
print(yeardict)
most_yr=max(yeardict,key=lambda d:yeardict.get(d))
print(most_yr)