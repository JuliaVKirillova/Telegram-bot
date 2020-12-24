import os
import telegram
import time
import requests
from dotenv import load_dotenv 

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
URL = os.getenv('URL')
V = os.getenv('VK_API_VERSION')  
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
id_1 = os.getenv('id_1')

def get_user_status(user_id):
    params = {
        'user_ids': user_id,
        'fields': 'online',
        'v': V,
        'access_token': ACCESS_TOKEN
    }
    try:
        user_status = requests.post(URL, params=params).json()['response'][0]['online']
        user_name = requests.post(URL, params=params).json()['response'][0]['first_name']
        return user_status, user_name
    except requests.exceptions.RequestException as e:
        logging.exception(f'Request raised error: {e}')  



def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    return bot.send_message(chat_id=CHAT_ID, text=message)



if __name__ == "__main__":
    vk_id = id_1
    while True:
        status, name = get_user_status(vk_id)
        if status == 1:
            send_message(f'{name} сейчас онлайн!')
            break
        time.sleep(1200)