import json

data = open('./badword.json',r)

for i in data:
    if i in user_data:
        return "욕확인"