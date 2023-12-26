#!/usr/bin/env python3
import os
import glob
import time


number_files = len(glob.glob1('.',"*.jpg"))
today = time.strftime("%Y-%m-%d")
time_now = time.strftime("%H:%M:%S")

html = "<!DOCTYPE html>\n<html>\n<head>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n</head>\n<body>\n"
html += f"<center><b>Total terminals listed: " + str(number_files) + "</b>\n"
html += f"<center><b>Last run script date: " + today + "</b>\n"
html += f"<center><b>Last run script time: " + time_now + "</b>\n"
html += f"<center><b>" + "-------" + "</b>\n"

for file in glob.glob("*.jpg"):
        #html += f"<b>" + file + "</b>"
        #html += f"<img src='{file}' width='10%' height='10%'><br>"
        html += f"<center><b>" + file + "</b>"
        html += f"<center><img src='{file}' width='30%' height='30%'></center><br>"

html += "</body>\n</html>"

with open("index.html", "w") as outputfile:
        outputfile.write(html)
  
