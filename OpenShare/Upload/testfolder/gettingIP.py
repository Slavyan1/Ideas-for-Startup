# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:08:25 2020

@author: slavy
"""

import netifaces

interfaces = netifaces.interfaces()

for i in interfaces:
    if i == 'lo':
        continue
    iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    if iface != None:
        for j in iface:
            print(j['addr'])
            
            