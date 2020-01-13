import requests
import threading
import config

def get_hosts():
    hosts = []
    done = 0
    
    def update(i):
        try:
            hosts.append(requests.get(config.URL % i, timeout=5).url)
        except:
            pass
        
        nonlocal done
        done += 1
        
    for i in range(256):
        threading.Thread(target=update, args=(i,)).start()
    
    while done != 256:
        pass
    
    return hosts

print(get_hosts())
    
