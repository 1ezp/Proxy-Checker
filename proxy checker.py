import os
from threading import Thread
try:
    import requests
except:
    os.system("pip install requests")
from termcolor import colored
r = requests.session()

proxy_file = open('proxyies.txt','r').read()

def check(url,proxy):
    r.proxyies = {
        'http': 'http://{}'.format(proxy),
        'https':'{}'.format(proxy)
    }
    try:
        g= r.get(url)
        if g.status_code == 200:
            print(colored(f"[+] {proxy}",'green'))
            save = open('Good.txt','a')
            save.write("{}\n".format(proxy))
        else:
            print(colored(f"[-] {proxy}",'red'))
    except:
        print(colored(f"[-] {proxy} Bad",'red'))
if __name__ == "__main__":
    url = input(colored("URL: ","blue"))
    for i in proxy_file.splitlines():
        check(url,i)
        #Thread(target=check,args=(url,i)).start()
