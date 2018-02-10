from weather import Weather, Unit
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if(config['WEATHER']['units'] =='CELSIUS'):
	units=Unit.CELSIUS
else:
	units=Unit.FAHRENHEIT

w =Weather(units)
woeid=int(config['WEATHER']['woeid'])
data = w.lookup(woeid)

def getConditions(data):
	now = data.condition()
	output = list()
	output.append(now.text())
	output.append(now.temp())
	output.append(now.code())
	output.append(now.date())
	output.append(data.wind())
	return output

results=getConditions(data)

for result in results:
	print(result)
