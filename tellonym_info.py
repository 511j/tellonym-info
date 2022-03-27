# Codeing by lord4tb , [ @ilord4tb ]
# github : 511j
# Free src in >> https://github.com/511j/tellonym-info

from distutils.log import error
import os,time,datetime,requests
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()
#os.system("title Tellonym info Developed by : @ilord4tb - Lord4tb .#4465")
class ON():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"#Green +
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]" #Blue +
    redplus = f"{WHITE}[ {RED}+{WHITE} ]" #Red +
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    loblue = f"\n{WHITE}[ {BLUE}*{WHITE} ] Tellonym info {BLUE}- {WHITE}Follow me in instagram{BLUE} : {WHITE}{BLUE}@{WHITE} iLord4tb {BLUE}..{WHITE}"
class lord4tb():
    def __init__(self):
        print(ON.loblue)
    def inex(self):
        print(f"\n{ON.redminus} Press Enter To Exit : ", end=f"{ON.BLUE}")
        input()
        exit()
def banner ():
    print(f'''
{ON.WHITE}  ::::::::::: {ON.RED}::::::::::{ON.RED} :::        {ON.WHITE}:::        ::::::::  ::::    :{ON.BLUE}:: :::   :::  :::   :::    
{ON.BLUE}     :+:    {ON.RED} :+:        :+:        {ON.WHITE}:+:       :+:    :+: :+:+:   :+: {ON.BLUE}:+:   :+: :+:+: :+:+:    
{ON.BLUE}    +:+    {ON.RED} +:+        +:+        {ON.WHITE}+:+       +:+    +:+ :+:+:+  +:+  {ON.BLUE}+:+ +:+ +:+ +:+:+ +:+    
{ON.BLUE}   +#+     {ON.RED}+#++:++#   +#+        {ON.WHITE}+#+       +#+    +:+ +#+ +:+ +#+   {ON.BLUE}+#++:  +#+  +:+  +#+     
{ON.BLUE}  +#+     {ON.RED}+#+        +#+        {ON.WHITE}+#+       +#+    +#+ +#+  +#+#+#    {ON.BLUE}+#+   +#+       +#+      
{ON.BLUE} #+#    {ON.RED} #+#        #+#        {ON.WHITE}#+#       #+#    #+# #+#   #+#+#    {ON.BLUE}#+#   #+#       #+#       
{ON.BLUE}###     {ON.RED}########## ########## {ON.WHITE}########## ########  ###    ####    {ON.BLUE}###   ###       ###        
{ON.BLUE}                   ::::::::::: {ON.WHITE}::::    ::: :::::::::: ::::::::                               
{ON.BLUE}                      :+:     {ON.WHITE}:+:+:   :+: :+:       {ON.BLUE}:+:    :+:                               
{ON.BLUE}                     +:+     {ON.WHITE}:+:+:+  +:+ +:+       {ON.BLUE}+:+    +:+                                
{ON.BLUE}                    +#+     {ON.WHITE}+#+ +:+ +#+ :#::+::#  {ON.BLUE}+#+    +:+                                 
{ON.BLUE}                   +#+     {ON.WHITE}+#+  +#+#+# +#+       {ON.BLUE}+#+    +#+                                  
{ON.BLUE}                  #+#     {ON.WHITE}#+#   #+#+# #+#       {ON.BLUE}#+#    #+#                                   
{ON.BLUE}             ########### {ON.WHITE}###    #### ###        {ON.BLUE}########''')
        
os.system("clear")
banner()
x = lord4tb()
    
def inf():
    username = input(f"\n{ON.blueplus} Enter username : {ON.BLUE}")
    os.system("clear")
    banner()
    x = lord4tb()
    #os.system("title info panel Developed by : @ilord4tb - Lord4tb .#4465")
    url = f'https://api.tellonym.me/profiles/name/{username}?previousRouteName=FeedFeatured&isClickedInSearch=false&sourceElement=People%20Suggestion&adExpId=94&limit=16'
    headers = {
        'Host': 'api.tellonym.me',
        'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="92"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    req = requests.get(url, headers=headers)
    print(f'\n{ON.blueplus} Country Code : {ON.BLUE}' + req.json()['countryCode'])
    print(f'{ON.WHITE}{ON.blueplus} Name : {ON.BLUE}' + req.json()['displayName'])
    print(f'{ON.WHITE}{ON.blueplus} Profile Pic : ' + f'{ON.BLUE}https://userimg.tellonym.me/xs/' + req.json()['avatarFileName'])

inf()
x.inex()
