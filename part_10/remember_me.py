# -*- coding: cp936 -*-
# ʹ��json.dump()�洢����

import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
   json.dump(username, f_obj)
   print("We will remember you when you come back, " + username + "!")
   




    
