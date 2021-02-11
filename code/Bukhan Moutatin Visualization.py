# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:02:13 2019

Visualization Bukhan Mountain Ecosystem

@author: jaewoong Han
"""

import pandas as pd
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import pyplot as plt
import folium
from gmplot import gmplot
import webbrowser
import csv

forest = pd.read_csv('csv_file', encoding='euc-kr')

# 위도, 경도 조절
forest['위도']=forest['도']+forest['분']/60+forest['초']/3600
forest['경도']=forest['도.1']+forest['분.1']/60+forest['초.1']/3600

# 수정본 저장
forest.to_csv('./forest2.csv', sep=',', encoding='euc-kr')

# 다시 부른 뒤 html 시각화
from gmplot import gmplot
import webbrowser
import csv

filename = 'forest2.csv'

lats,lons, month=[],[], []

with open(filename) as f:
    reader = csv.reader(f)
    #ignore first line header
    next(reader)
    for row in reader:
        lats.append(float(row[10]))
        lons.append(float(row[11]))

# Place map bukhansan
gmap = gmplot.GoogleMapPlotter(37.662871, 126.9932290, 13) # 북한산 위도, 경도 위치

# Scatter Drawing
gmap.scatter( lats, lons, '#4c00ff',s=month, size = 20, marker = False )
             
# Draw
gmap.draw("my_map.html")

# Run Browser
webbrowser.open_new("my_map.html")
