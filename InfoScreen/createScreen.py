#generate an html file using python
from weatherinfo import getWeather
from fileStuff import *
f = open('screen.html','w')
weather=getWeather()
weatherText= htmlList(weather)

message = """<html>
<head>InfoScreen</head>
<body>
<h2>Weather Report</h2>
"""+ weatherText+"""
</body>
</html>
"""

f.write(message)
f.close()