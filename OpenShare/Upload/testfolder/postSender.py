# -*- coding: utf-8 -*-

"""
Created on Thu Dec 26 18:57:43 2019

@author: Славян
"""

import configparser
import smtplib                                      
from email.mime.multipart import MIMEMultipart      
from email.mime.text import MIMEText                
from email.mime.image import MIMEImage     

path   = 'settings.ini'
config = configparser.ConfigParser()
config.read(path)

addr_from = config.get('Settings', 'addr_from')         
password  = config.get('Settings', 'password') 
addr_to   = "kill0314@yandex.com"                   
                       

msg = MIMEMultipart()                               
msg['From']    = addr_from
msg['To']      = addr_to                            
msg['Subject'] = 'Test'                             

body = "Ведьмаку заплатите, чеканной монетой"
msg.attach(MIMEText(body, 'plain'))                 

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()                                   
server.login(addr_from, password)
server.send_message(msg)                            
server.quit()     

