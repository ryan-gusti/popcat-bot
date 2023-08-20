import requests
import time

URL_POP = "https://stats.popcat.click/pop?"
URL_DATA = "https://leaderboard.popcat.click"

pop_count = int(input("😾 Amount pops (1-800) = "))
token = input("🔒 Token = ")
t = int(input("⌛ Delay = "))

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
    print('🦾 Execute')
    post_data = requests.post(url=URL_POP, data=data)
    result(post_data.status_code)
    print('🦾 Getting Data')
    get_data = requests.get(url=URL_DATA)
    total = get_data.json()
    indonesia = total['ID']
    print("🚨 {:,}".format(indonesia))