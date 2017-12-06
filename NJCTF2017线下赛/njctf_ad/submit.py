import requests



def submit(flag):
    r = requests.post("http://172.16.100.5:9000/submit_flag/", data={
        "flag": str(flag),
        "token": "LL4wdEeeRRWtOT2bSLn4dxBmjmGZfJujEdqsIRguMjQd33Bcv9gyuoDREv49ZK1YhtKOAKFwPbM"
    })
    print r.text


if __file__ == "__main__":
    submit("test")