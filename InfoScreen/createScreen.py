#generate an html file using python
from weatherinfo import getWeather
f = open('screen.html','w')
weather=getWeather()
weatherText= ''.join(map((lambda val: "<li>"+str(val)+"</li>\n"),weather))
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