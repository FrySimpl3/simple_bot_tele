
#pip install telethon
from telethon.sync import TelegramClient
import requests
import time
from datetime import datetime
#pip install pytz
import pytz

api_id = ''
api_hash = ''
bot_token = ''
webhook_url = ''

def send_to_webhook(data):
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Data sent to Discord webhook successfully.")
    else:
        print("Failed to send data to Discord webhook. Status code:", response.status_code)

with TelegramClient('session_name', api_id, api_hash) as client:
    channel = client.get_entity('https://t.me/channel')
    last_message_date = datetime(2023, 11, 12, tzinfo=pytz.UTC)  # Set the date to filter messages.

    while True:
        try:
            messages = client.get_messages(channel, limit=None)

            for message in reversed(messages):
                if message.date > last_message_date:
                    formatted_date = message.date.strftime("[ %H:%M:%S %d-%m-%Y ]")
                    data = {
                        'content': f"{formatted_date} <@&1173261936092258355> \n {message.text}\n",
                        'username': 'Fry',
                    }
                    send_to_webhook(data)
                    last_message_date = message.date

            time.sleep(1)  # Wait for 1 second before checking for new messages again.
        except Exception as e:
            print("An error occurred:", str(e))
