import json
import re
import requests
from twilio.rest import Client

account_SID = "<SID>" #replace with SID
auth_token = "<token>" #replace with authtoken
twilio_cli = Client(account_SID, auth_token)
twilio_num = "<num>" #replace with twilio number
phone_num = "<num>" #replace with personal number

f = open("auth.log", "r")
connected_ips = ""
for line in f:
    has_connected = ""
    has_connected = re.search("Accepted publickey", line)
    if has_connected:
        has_connected_ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        connected_ip = has_connected_ip.group(0)
        connected_ips += connected_ip + " "
connected_ips = connected_ips.split()
for ip in connected_ips:
    if ip != "<ip>" and ip != "<ip>": #replace with personal ips
        ip_info = requests.get("http://ip-api.com/json/" + ip)
        python_json = json.loads(ip_info.text)
        location = python_json["city"]
        message = "Login to <server> from " + location #replace with server name
        twilio_cli.messages.create(body=message, from_=twilio_num, to=phone_num)
         
f.close()
