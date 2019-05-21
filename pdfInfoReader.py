#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:28:09 2019

@author: anilosmantur
"""

import PyPDF2 as pdf
import pandas as pd
import os

data = {'file_name' : [],
        'DOI' : [],
        'title' : [],
        'key_1' : [],
        'key_2' : [],
        'key_3' : [],
        'key_4' : [],
        'key_5' : []}

rootDir = 'papers'
fileNames = os.listdir(rootDir)

for fileName in fileNames:
    data['file_name'].append(fileName)
    pdfHead = pdf.PdfFileReader(os.path.join(rootDir, fileName))
    info = pdfHead.documentInfo
    
    data['DOI'].append('https://doi.org/' + info['/doi'])
    data['title'].append(str(info['/Title']))
    try:
        keys = info['/Keywords'].split(',')
        for i in range(1, 6):
            try:
                data['key_{}'.format(i)].append(keys[i-1])
            except:
                data['key_{}'.format(i)].append(' ')
    except:
        print('no keyword element entered')
        print(fileName)
    

df = pd.DataFrame(data)
df.to_csv('papers_table.csv')
