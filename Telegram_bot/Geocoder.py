import geocoder
import pyowm

# URL ССЫЛКА НА МЕСТО
def geo(name_city):
    result = geocoder.arcgis(name_city)
    result = result.latlng
    result ='https://www.google.ru/maps/place/'+ str(result[0]) + ',' + str(result[1])
    return result

# ОПРЕДЕЛИТЬ ГДЕ НУЖНО ИСКАТЬ
def weather_observation(name_city):
    own = pyowm.OWM('8028c9c043bf428d13478fde2feda3cf', language='ru')
    observation = own.weather_at_place(name_city)
    WEATHER = observation.get_weather()
    return WEATHER

# СТАТУС ПОГОДЫ
def weather_stats(name_city):
    WEATHER = weather_observation(name_city)
    WEATHER_detailed =WEATHER.get_detailed_status()
    return 'Сейчас в "{}" : '.format(name_city) + WEATHER_detailed

# ТЕМПЕРАТУРА
def weather_temperature(name_city):
    WEATHER = weather_observation(name_city)
    WEATHER_temperature = WEATHER.get_temperature('celsius')
    WEATHER_TEMPERATURE_MIDDLE = WEATHER_temperature['temp']
    return 'Сейчас в "{}" температура по цельсию: '.format(name_city) + str(WEATHER_TEMPERATURE_MIDDLE)

# СКОРОСТЬ ВЕТРА
def weather_wind(name_city):
    WEATHER = weather_observation(name_city)
    WEATHER_WIND = WEATHER.get_wind()
    return 'Скорость ветра в "{}" : '.format(name_city) + str(WEATHER_WIND['speed']) + 'м/c'