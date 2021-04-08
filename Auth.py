#pip3 install discord-webhook
#pip3 install PyAuthGG
#pip3 install requests

import PyAuthGG
import json
import requests
from discordwebhook import Discord

API = 'API KEY'
AID = 'AID KEY'
SECRET = 'SECRET KEY'
webhook = 'WEBHOOK'

Admin = PyAuthGG.Administration(API)
App = PyAuthGG.Application(API, AID, SECRET)

print("""

1. Gather User Info
2. Reset HWID
3. Ban User
4. Dump Data
5. User Count """)

test_options = input("Option: ")

#User information function
if test_options == "1":
        username = input("Username: ")
        req = Admin.FetchUser(username)
        print(Admin.FetchUser(username))
        with open(f'{username}.txt', 'w') as f:
            json.dump(req, f, indent=2)

#HWID reset function
if test_options == "2":
        hwid = input("Username: ")
        Admin.ResetHWID(hwid)
        print("f{hwid} has been reset!")
        discord = Discord(url=webhook)
        discord.post(embeds=[
        {
            "author": {
                "name": "Obstacles - Auth Control",
                "url": "https://instagram.com/experienced",
                "icon_url": "https://media-cdn.tripadvisor.com/media/photo-p/0d/31/18/5e/pure.jpg",
            },
            "title": "",
            "description": f"The user {hwid} has been given a HWID reset!",
            "image": {"url": "https://media.giphy.com/media/sChf4Eo55W8x2/giphy.gif"},
            "footer": {
                "text": "Obstacles - Auth Control",
            },
        }
    ],
)

#Delete user aka ban function
if test_options == "3":
        ban = input("Username: ")
        Admin.DeleteUser(ban)
        print("f{ban} has been banned!")
        discord = Discord(url=webhook)
        discord.post(embeds=[
        {
            "author": {
                "name": "Obstacles",
                "url": "https://instagram.com/experienced",
                "icon_url": "https://media-cdn.tripadvisor.com/media/photo-p/0d/31/18/5e/pure.jpg",
            },
            "title": "",
            "description": f"The user {ban} has been banned!",
            "image": {"url": "https://media.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif"},
            "footer": {
                "text": "Obstacles - Auth Bot",
            },
        }
    ],
)


#Dumping all data in Auth.GG project
if test_options == "4":
    r = requests.get(f"https://developers.auth.gg/USERS/?type=fetchall&authorization={API}").json()
    print("Saving output!")
    with open('data.txt', 'w') as f:
        json.dump(r, f, indent=2)

#User Count Function
if test_options == "5":
    re = requests.get(f"https://developers.auth.gg/USERS/?type=count&authorization={API}").json()
    print("Checked usercount!")
    discord = Discord(url=webhook)
    discord.post(embeds=[
    {
        "author": {
            "name": "Obstacles",
            "url": "https://instagram.com/experienced",
            "icon_url": "https://media-cdn.tripadvisor.com/media/photo-p/0d/31/18/5e/pure.jpg",
        },
        "title": "",
        "description": f"User Count: {re}",
        "image": {"url": "https://media.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif"},
        "footer": {
            "text": "Obstacles - Auth Bot",
        },
    }
],
)
