import requests
import webbrowser

import threading

import config
   
def update(i):
    try:
        r = requests.get((config.URL + "/info") % i, timeout=5)
        if r.text.startswith("OpenShare Server"):
            webbrowser.open_new(config.URL % i)
            
    except:
        pass
        
for i in range(256):
    threading.Thread(target=update, args=(i,)).start()

    
