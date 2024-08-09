from selenium.webdriver import Chrome
import json

def getcookies():
    web = Chrome()
    web.get('https://www.bilibili.com/')
    sr=input("请先登录，登录完成后按回车继续：")
    print("当前cookie：")
    cookies = web.get_cookies()
    for cookie in cookies:
        print(cookie)
    cookies_json = json.dumps(cookies, indent=4)
    with open(r'cookies.json', "w") as f:
        f.write(cookies_json)   
    print("\n以上cookies已保存在cookie.json")
    web.quit()