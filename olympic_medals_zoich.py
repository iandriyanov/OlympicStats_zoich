#-*- coding: utf-8 -*-

############################################
#
# File Name : olympic_medals_zoich.py
#
# Purpose :
#
# Creation Date : 11-02-2014
#
# Last Modified : Wed 12 Feb 2014 08:59:39 AM MSK
#
# Created By : plushka
#
############################################


# http://olympics.clearlytech.com/api/v1/medals
import requests

req = requests.get("http://olympics.clearlytech.com/api/v1/medals")

header = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
<table border="1" width="35%">
  <tr>
    <td>СТРАНА</td>
    <td>Золото</td>
    <td>Серебро</td>
    <td>Бронза</td>
    <td>ИТОГ</td>
    <td>МЕСТО</td>
  </tr>
"""

footer = """
</table>
</body>
</html>
"""

with open("res.html", "w") as f:
    f.write(header)
    for answer in req.json():
        if answer[u'rank'] > 0 and answer[u'rank'] <= 10:
            f.write("""
  <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
  </tr> """ % (answer[u'country_name'], answer[u'gold_count'], answer[u'silver_count'], answer[u'bronze_count'], answer[u'medal_count'], answer[u'rank']))
    f.write(footer)
