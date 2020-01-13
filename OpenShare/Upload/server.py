from flask import Flask, escape, request, send_file
import netifaces

import os

import config

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/download')
def hello():
    text = ""
    for filename in os.listdir(config.FOLDER):
        text += "<a href='{filename}'>{filename} [{stat} Mb]</a><br>".format(
                filename=filename, stat=round(os.stat(filename)[6]*0.00000095367432, 3)
        )
        
    if not text:
        return "No once file in directory"
    
    return text

@app.route('/version')
def version():
    return '1'

@app.route('/<filename>')
def get_file(filename):
    if filename not in os.listdir(config.FOLDER):
        return 'File not in directory'
    
    return send_file(filename)

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

app.run(host, 1337)