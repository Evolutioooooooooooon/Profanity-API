import json

data = open('./badword.json','r')

user_data = "시발"

for i in data:
    if i in user_data:
        print("욕 확인")