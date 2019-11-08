import pyowm
import telebot
owm = pyowm.OWM("cfade00ca1f4fd527a497ff66c591dee",language= "ru")
bot =  telebot.TeleBot("1007527721:AAG8ZmZDdncHvggGR1XIiHuwJighi0Z9mtc")
@bot.message_handler( content_types= ["text"])
def send_echo(message):
    observation =  owm.weather_at_place( message.text)
    w =  observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    answer ="В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n" 
    answer +="Температура сейчас в районе" + str(temp) + "\n\n"
    if temp < 10:
        answer += ("Суйчас ппц как холодно,если не хочешь умереть оденься потеплее")
    elif temp < 20:
        answer += ("сейчас холодно хорошо оденься иначе твоей маме позвоню")
    else:
        answer += ("температу зашибись иди цыплять тяночек")
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True )

