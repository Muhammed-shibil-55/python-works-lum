enquiries=["django","testing","django","bigdata","aws","aws","django","django"]
courses={}
for en in enquiries:
    if en in courses:
        courses[en]+=1
    else:
        courses[en]=1
print(courses)