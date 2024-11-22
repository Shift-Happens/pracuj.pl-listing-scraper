import os
from dotenv import load_dotenv
from telegram import Bot
import asyncio

# Load environment variables
load_dotenv()

async def test_telegram_connection():
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    try:
        me = await bot.get_me()
        print(f"Bot connection successful. Bot name: {me.first_name}")
        
        await bot.send_message(
            chat_id=os.getenv('TELEGRAM_CHAT_ID'),
            text="Test message from job scraper"
        )
        print("Test message sent successfully")
    except Exception as e:
        print(f"Error: {str(e)}")

def send_telegram_message(message):
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    asyncio.run(bot.send_message(
        chat_id=os.getenv('TELEGRAM_CHAT_ID'),
        text=message
    ))

def notify_new_offers(new_offers):
    if new_offers:
        message = "New job offers:\n"
        for offer in new_offers:
            message += f"{offer['title']} at {offer['company']}\n"
        send_telegram_message(message)