import telebot
import requests
import json
from config import keys, TOKEN
from extensions import ConvertionException


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'Чтобы начать работу введите комманду боту в слудеющем формате:\n <имя валюты> \
<в какую валюту перевести \n доступные валюты /values >\
<количество переводимой валюты>*')

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты: "
    for key in keys.keys():
        text = '\n '.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
          raise ConvertionException('Слишком много параметров')
        quote, base,  amount = values
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалосб отработать команду \n {e}')
    else:


        r = requests.get( f'https://currate.ru/api/?get=rates&pairs={keys[quote]}{keys[base]}&key=9ee019ad5bd05bc0e789d5f875e3e750')
        text = json.loads(r.content)
        n = text['data'][f'{keys[quote]}{keys[base]}']
        converted_amount = float(amount)
        converted_n = float(n)
        fin = converted_amount * converted_n
        bot.send_message(message.chat.id, f'Cyмма {amount} {quote} в {base} = {fin}' )



bot.polling(none_stop=True, interval=0)


