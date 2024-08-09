from getcookie import getcookies
from loadcookie import loadcookies
from bomber import bomber

while(True):
    print("请选择：1.获取cookie   2.使用现有cookie   3.帮助")
    select=input("请输入选项：")
    if (int(select)==1):
        getcookies()
    if (int(select)==2):
        cookies=loadcookies()
        print("当前cookies:")
        for cookie in cookies:
            print(cookie)
        try:    
            bomber(cookies)
        except Exception as e:
            print(e)
            print("\n出现错误，请检查是否登录账号或步骤是否正确,也可能是因为网页等待超时")
            break
    if (int(select)==3):
        text=open(r'help.txt','r',encoding='utf8')
        helptext=text.read()
        text.close()
        print(helptext+"\n")