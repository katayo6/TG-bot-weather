from pyowm.utils.config import get_default_config
from pyowm import OWM 
import telebot  
import time
config_dict = get_default_config()
config_dict['language'] = 'ru' 
botToken = 'TGBOTTOKEN'
bot = telebot.TeleBot(botToken)
owm = OWM('OPENWEATHERTOKEN', config_dict)
@bot.message_handler(content_types=['text'])
def send_message(message):
	try:
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place('Kurgan,RU') # City, Country
		weather = mgr.weather_at_place('Kurgan,RU').weather 
		w = observation.weather
		temp = weather.temperature('celsius')['temp']
		wind = w.wind(unit='meters_sec')
		answer = "В Кургане сейчас " + weather.detailed_status + '\n\n'
		answer +='Ветер: ' + str(int(wind['speed'])) + ' м/с' + '\n\n'
		answer += 'Температура на данный момент: '  + str(int(temp))  + "°С" + '\n\n'
		print(time.ctime(), "User id:", message.from_user.id)
		print(time.ctime(), "Message:", message.text.title())
	except Exception:
            		print(time.ctime(), "User id:", message.from_user.id)
            		print(time.ctime(), "Message:", message.text.title())
	bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True)

