from weather import Weather, Unit
import configparser
def getWeather():
	config = configparser.ConfigParser()
	config.read('config.ini')
	if(config['WEATHER']['units'] =='CELSIUS'):
		units=Unit.CELSIUS
	else:
		units=Unit.FAHRENHEIT

	w =Weather(units)
	woeid=int(config['WEATHER']['woeid'])
	data = w.lookup(woeid)

	results=getConditions(data)
	return results




def getConditions(data):
	now = data.condition()
	output = list()
	output.append(now.text())
	output.append(now.temp())
	output.append(now.code())
	output.append(data.wind())
	output.append(now.date())
	return output

if __name__ == "__main__": getWeather()