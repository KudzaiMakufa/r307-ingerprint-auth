import requests

# payload = { 'operation':'transfer' ,'account':posid,'amount':amount , 'date':datetime.datetime.now()}
r=requests.post('http://127.0.0.1:8000/home/api_login/', auth=("admin", "qwertypass" ), data={'username':"admin" ,"password":"qwertypass"})


print(r)