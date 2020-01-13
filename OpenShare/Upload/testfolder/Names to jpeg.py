# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:40:41 2020

@author: slavy
"""

import os


for file in os.scandir('D:\\tgphoto\\'):
    if not file.name.endswith(".jpeg"):
        os.renames(file.path, file.path + '.jpeg')