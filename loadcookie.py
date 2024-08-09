import json

def loadcookies():
    try:
        with open(r'cookies.json', "r") as f:
            cookies = json.load(f)
            return cookies
    except Exception as e:
            print("出现错误，请检查使用该程序的步骤是否正确")
