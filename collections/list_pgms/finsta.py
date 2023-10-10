all_users=["mammootty","mohanlal","kunchako boban","dileep","tovino","asif ali","dq","fahad","vijay","jayasurya"]
dileep_friends=["mohanlal","kunchako boban","jayasurya"]
suggest=[]
for a in all_users:
    if a not in dileep_friends and a!="dileep":
        suggest.append(a)
print("suggestions :-")
for s in suggest:
       print(s)