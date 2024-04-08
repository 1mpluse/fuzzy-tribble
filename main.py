import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7178237793:AAG7r6GmjzkdRf0vo2wxt2T7e7_69b6R1AY'

MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет


    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()


    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']

            type_message = result['message']

            if type_message.get('text'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text= Ого! ты мне прислал текст! ')
            elif type_message.get('sticker'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text= Ого! ты мне прислал стикер! ')
            elif type_message.get('photo'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text= Ого! ты мне прислал фото! ')
            elif type_message.get('video'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text= Ого! ты мне прислал видео! ')
            elif type_message.get('voice'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text= Ого! ты мне прислал голосовое сообщение! ')
    time.sleep(1)
    counter += 1