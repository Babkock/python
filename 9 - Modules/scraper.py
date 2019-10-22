#!/usr/bin/python3
import requests

url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=201903&Campus=1;4&S'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()

