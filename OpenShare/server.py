from flask import Flask, escape, request, send_file, render_template, redirect
import netifaces
import hashlib
import webbrowser

import os

import config

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/download')

@app.route('/download')
def hello():
    filenames = []
    for entity in os.scandir(config.FOLDER):
        if not entity.is_file():
            continue
        
        filenames.append({"name": entity.name, "size": round(entity.stat().st_size*0.00000095367432, 3)})
    
    return render_template('downloads.html', filenames=filenames)

@app.route('/<filename>')
def get_file(filename):
    if filename not in os.listdir(config.FOLDER):
        return 'File not in directory'

    return send_file(config.FOLDER+'\\'+filename)

@app.route('/down_all')
def down_all():
    for entity in os.scandir(config.FOLDER):
        if not entity.is_file():
            continue
        
        return send_file(config.FOLDER+'\\'+entity.name)
        

@app.route('/info')
def iformation():
    return 'OpenShare Server'

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
    
webbrowser.open_new("http://"+host+":"+str(config.PORT))
app.run(host, config.PORT)