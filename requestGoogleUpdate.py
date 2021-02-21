# -*- coding: utf-8 -*-
import webbrowser

"""
Little script that replaces comment characters to html,
found in the *.hbs files.
"""

import os
import requests

url = "http://www.google.com/ping?sitemap=https://mond-al.github.io/sitemap.xml"
fileName = "requestResult.html"
if os.path.exists(fileName):
    os.remove(fileName)
f = open(fileName, mode='wt')

res = requests.get(url)
f.write(res.text)
print(res.status_code)
