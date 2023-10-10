all_users=["sachin","kohli","rahul","rohit","dravid","laxman","ganguly"]
sachin_following=["rahul","ganguly","dravid"]
sachin_suggest=set(all_users).difference(set(sachin_following))
sachin_suggest.remove("sachin")
print(sachin_suggest)