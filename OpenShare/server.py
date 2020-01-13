from flask import Flask, escape, request, send_file
import netifaces
import hashlib

import os

import config

app = Flask(__name__)

@app.route('/download')
def hello():
    text = ""
    for entity in os.scandir(config.FOLDER):
        if not entity.is_file():
            continue
    
        text += "<a href='{name}'>{name} [{size} Mb]</a><br>".format(
            name=entity.name, size=round(entity.stat().st_size*0.00000095367432, 3)
        )
        
    if not text:
        return "No once file in directory"
    
    return text

@app.route('/<filename>')
def get_file(filename):
    if filename not in os.listdir(config.FOLDER):
        return 'File not in directory'
    
    return send_file(config.FOLDER , filename)

# Preparing to Uploading
if config.CLEAN:
    os.system('rmdir /S /Q %s' % config.FOLDER) # Remove Upload
    os.system('mkdir %s' % config.FOLDER) # Create Upload
    print(" * Upload folder has been cleaned")

# Init Flask-Server
netfaces = []
for i in netifaces.interfaces():
    if i == 'lo':
        continue
    iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    if not iface:
        continue
    
    for data in iface:
        netfaces.append(data['addr'])

host = None
for h in netfaces:
    if h.startswith('192.168.'):
        host = h
        
print(" * Hosted on", host, "port:", config.PORT)
app.run(host, config.PORT)