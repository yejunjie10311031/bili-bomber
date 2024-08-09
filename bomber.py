from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def bomber(cookies):
    opt = ChromeOptions()
    service=Service(r'chromedriver.exe')
    opt.add_experimental_option('detach',True)
    web=Chrome(options=opt,service=service)
    web.get('https://www.bilibili.com/')
    time.sleep(1)
    for cookie in cookies:
        web.add_cookie(cookie)
    web.get('https://www.bilibili.com/')
    time.sleep(1)
    find=input("输入搜索内容：")
    search=web.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[1]/input').send_keys(find,Keys.ENTER)
    web.switch_to.window(web.window_handles[-1])
    time.sleep(1)
    num=1
    url = web.current_url
    page=input("输入页数：")
    if int(page)==1:
        url=url
    else:
        url=url+"&page="+page
        web.get(url)
        time.sleep(1)
    reply=input("输入回复内容：")    
    if int(page)==1:
        videos=web.find_elements(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[4]/div/div')
    else:
        videos=web.find_elements(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div')
    script = f"""
    let outerElement = document.querySelector('bili-comments');
    let outerShadowRoot = outerElement.shadowRoot;

    let innerElement = outerShadowRoot.querySelector('bili-comments-header-renderer');
    let innerShadowRoot = innerElement.shadowRoot;

    let innerElement2 = innerShadowRoot.querySelector('bili-comment-box');
    let innerShadowRoot2 = innerElement2.shadowRoot;

    let targetElement = innerShadowRoot2.querySelector('#editor');
    targetElement.click();

    let innerElement3 = innerShadowRoot2.querySelector('bili-comment-textarea');
    let innerShadowRoot3 = innerElement3.shadowRoot;

    let input = innerShadowRoot3.querySelector('#input');
    input.value = '{reply}';
    let event = new Event('input', {{ bubbles: true }});
    input.dispatchEvent(event);

    setTimeout(() => {{
        let send = innerShadowRoot2.querySelector('#pub button');
        send.click();
    }}, 100);
    """
    for video in videos:
        if int(page)==1:
            vi=web.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[4]/div/div['+str(num)+']/div/div/div/div/a/h3').text
            print(vi)
            linktem=web.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[4]/div/div['+str(num)+']/div/div/div/div/a')
            link=linktem.get_attribute('href')
            print(link)
        else:
            vi=web.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div['+str(num)+']/div/div/div/div/a/h3').text
            print(vi)
            linktem=web.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div['+str(num)+']/div/div/div/div/a')
            link=linktem.get_attribute('href')
            print(link) 
        web.execute_script(f"window.open('{link}', '_blank');")
        web.switch_to.window(web.window_handles[-1])
        time.sleep(7)
        try:
            web.execute_script(script)
            print("已发送评论："+reply)
            time.sleep(0.5)
        except Exception as e:
            print(e)
            continue
        web.close()
        web.switch_to.window(web.window_handles[-1])
        num+=1