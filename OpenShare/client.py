import requests
import threading
import config

hosts = []
done = 0
   
def update(i):
    try:
        r = requests.get((config.URL + "/info") % i, timeout=5)
        if r.text.startswith("OpenShare Server"):
            hosts.append(r.url)
            
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
    
