from pyowm.utils.config import get_default_config
from pyowm import OWM 
import telebot  
import time
config_dict = get_default_config()
config_dict['language'] = 'ru' 
botToken = '1800442691:AAGoUT24m4S0LQWA8o1saKRPuzEK0gc-aRU'
bot = telebot.TeleBot(botToken)
owm = OWM('9ba44acc75da89cee8a654c527d809ec', config_dict)
@bot.message_handler(content_types=['text'])
def send_message(message):
	  try:
	      mgr = owm.weather_manager()
	      observation = mgr.weather_at_place('Kurgan,RU')
	      weather = mgr.weather_at_place('Kurgan,RU').weather
	      w = observation.weather
	      temp = weather.temperature('celsius')['temp'] + 2
	      wind = w.wind(unit='meters_sec')
	      answer = "В Кургане сейчас " + weather.detailed_status + '\n\n'
	      answer +='Ветер: ' + str(int(wind['speed'])) + ' м/с' + '\n\n'
	      answer += 'Температура на данный момент: '  + str(int(temp))  + "°С" + '\n\n'
	      if temp < 20:
			     answer += 'Надень что-нибудь потеплее'
	      elif temp > 20:
		             answer += 'Надень что-нибудь полегче'
	      print(time.ctime(), "User id:", message.from_user.id)
	      print(time.ctime(), "Message:", message.text.title())
								
	  except Exception:
            		print(time.ctime(), "User id:", message.from_user.id)
            		print(time.ctime(), "Message:", message.text.title())

	
	  bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
