"""Always run this as administrator"""

import time
from datetime import datetime as dt

hosts_path=hosts #r"C:\Windows\System32\Drivers\etc\hosts"-actual file,use local hosts file for checking

redirect="127.0.0.1"

website_list=["www.example1.com","www.example2.com"]

while True:
    if 10 < dt.now().hour < 16:
        print("Working Hours")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun Hours")
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
