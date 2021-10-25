import json
import re
import requests
from twilio.rest import Client

account_SID = "ACeaa127dde1dedfec4192d8181e856b48"
auth_token = "648090640141a616c168670692708e0f"
twilio_cli = Client(account_SID, auth_token)
twilio_num = "+13202881378"
phone_num = "+12506151971"

f = open("auth.log", "r")
ips = ""
connected_ips = ""
for line in f:
    has_ip = ""
    has_ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
    if has_ip:
        ip = has_ip.group(0)
        ips += ip + " "
    has_connected = ""
    has_connected = re.search("Accepted publickey", line)
    if has_connected:
        has_connected_ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        connected_ip = has_connected_ip.group(0)
        connected_ips += connected_ip + " "
ips = ips.split()
connected_ips = connected_ips.split()
for ip in connected_ips:
    if ip != "199.247.247.70" and ip != "24.244.70.68":
        ip_info = requests.get("http://ip-api.com/json/" + ip)
        python_json = json.loads(ip_info.text)
        location = python_json["city"]
        message = "Login to paul.youthlearntocode.com from " + location
        twilio_cli.messages.create(body=message, from_=twilio_num, to=phone_num)
         
f.close()
