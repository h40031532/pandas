from email import header
from urllib import response
from wsgiref import headers
from firebase import firebase
import pandas as pd
import requests
import schedule
import time

db_url = 'https://temirobot-1-default-rtdb.firebaseio.com/'

firebase = firebase.FirebaseApplication(db_url, None)

line_url = "https://notify-api.line.me/api/notify"
token_eld = '3eXm7CWw6HTmKfI5ctAIO5IQ1mVYzaJNhrrfTkXhj0e'
token_user = '0zKvbS7FQx7prOLzQ49edqLJzgj1nMmfNWQ49gqWzS9'

checklist = firebase.get('/user', None)


##報到 for 個管師
    
namelist = []

for key,value in checklist.items():
    #print ("id={}\tname={}\tcheck_bool={}".format(key,value['name'],str(value['CheckIn'])))
    #dict1 = {key:[value['name'],str(value['CheckIn'])]}
    check_name = (value['name'])
        
    if (str(value['CheckIn']) == "False"):
        namelist.append(check_name)
        namelist_2 = "\n".join(namelist)
print(namelist_2)

headers = {
        "Authorization": "Bearer " + token_user,
        "Content-Type": "application/x-www-form-urlencoded"
        }
     
params = {"message": "\n今天早上沒報到的有：\n" + namelist_2 + "\n請趕快聯繫他們的家人"}

r = requests.post(line_url, headers=headers, params = params)


##報到 for 長者
    
namelist = []

for key,value in checklist.items():
    #print ("id={}\tname={}\tcheck_bool={}".format(key,value['name'],str(value['CheckIn'])))
    #dict1 = {key:[value['name'],str(value['CheckIn'])]}
    check_name = (value['name'])
        
    if (str(value['CheckIn']) == "False"):
        namelist.append(check_name)
        namelist_2 = "\n".join(namelist)

headers = {
        "Authorization": "Bearer " + token_eld,
        "Content-Type": "application/x-www-form-urlencoded"
        }
     
params = {"message": "\n" + namelist_2 + "\n哈囉~今天怎麼還沒來呢?"}
        
r = requests.post(line_url, headers=headers, params = params)
