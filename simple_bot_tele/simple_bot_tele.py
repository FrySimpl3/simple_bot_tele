#pip install telethon
from telethon.sync import TelegramClient
import requests
import time
from datetime import datetime
#pip install pytz
import pytz

api_id = '26055847'
api_hash = '3503565f5dad1823534c87df88769265'
bot_token = '6706798616:AAG32P2td6_8ZibtXe9vxyMxvmlFd9xa2sE'
webhook_url = 'https://discord.com/api/webhooks/1173245344755224650/Cbkf6Zwyw3n_IPsqb1g-EL542q3J6j8O-ox2czq4oMG6YSE9jIt21Obnqj1zusYaeviM'
link_chanel = 'https://t.me/pubgmvnh'

# Set your time zone to UTC+7
your_timezone = pytz.timezone('Asia/Bangkok')

def send_to_webhook(data):
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Data sent to Discord webhook successfully.")
    else:
        print("Failed to send data to Discord webhook. Status code:", response.status_code)

with TelegramClient('session_name', api_id, api_hash) as client:
    channel = client.get_entity(link_chanel)
    last_message_date = datetime(2023, 11, 12, tzinfo=pytz.UTC)

    while True:
        try:
            messages = client.get_messages(channel, limit=None)

            for message in reversed(messages):
                if message.date > last_message_date:
                    formatted_date = message.date.astimezone(your_timezone).strftime("[ %H:%M:%S %d-%m-%Y ]")
                    data = {
                        'content': f"{formatted_date} <@&1173261936092258355> \n {message.text}\n",
                        'username': 'Fry',
                    }
                    send_to_webhook(data)
                    last_message_date = message.date                                         
            time.sleep(120) 
        except Exception as e:
            print("An error occurred:", str(e))
