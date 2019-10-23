#!/usr/bin/python3
"""
Tanner Babcock
October 22, 2019
Module 9, topic 3: Web scraper
"""
import requests

url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=201903&Campus=1;4&S'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()

