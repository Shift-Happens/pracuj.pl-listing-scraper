import json
from telegram import Bot

def send_telegram_message(message):
    with open('config.json') as config_file:
        config = json.load(config_file)
    bot = Bot(token=config['telegram']['token'])
    bot.send_message(chat_id=config['telegram']['chat_id'], text=message)

def notify_new_offers(new_offers):
    if new_offers:
        message = "New job offers:\n"
        for offer in new_offers:
            message += f"{offer['title']} at {offer['company']}\n"
        send_telegram_message(message)