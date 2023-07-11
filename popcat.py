import requests
import time

URL = "https://stats.popcat.click/pop?"

pop_count = int(input("Amount pops (1-800) = "))
token = input("Token = ")
t = int(input("Delay = "))

data = {
    'pop_count' : pop_count,
    'token' : token
}

def timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("⌛",timer, end="\r")
        time.sleep(1)
        t -= 1

def result(code):
    if code == 201:
        print("✅ Success") 
    else:
        print("❌ Failed")

while True:
    timer(t)
    print('⚡ Execute')
    r = requests.post(url=URL, data=data)
    result(r.status_code)