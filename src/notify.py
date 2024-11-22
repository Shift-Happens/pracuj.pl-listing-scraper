import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.constants import ParseMode
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
            text="Test message from job scraper",
            parse_mode=ParseMode.MARKDOWN_V2
        )
        print("Test message sent successfully")
    except Exception as e:
        print(f"Error: {str(e)}")

async def send_message_async(bot, chat_id, text):
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"Error sending message: {str(e)}")

async def send_all_messages(messages):
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    for message in messages:
        await send_message_async(bot, chat_id, message)
        # Add small delay between messages
        await asyncio.sleep(0.5)

def send_telegram_messages(messages):
    asyncio.run(send_all_messages(messages))

def format_offer(offer):
    # Escape special characters for MARKDOWN_V2
    def escape_markdown(text):
        special_chars = '_*[]()~`>#+-=|{}.!'
        return ''.join(f'\\{c}' if c in special_chars else c for c in str(text))
    
    return f"""
*{escape_markdown(offer['title'])}*
🏢 *Company:* {escape_markdown(offer['company'])}
💰 *Salary:* {escape_markdown(offer['salary'] if offer['salary'] else 'Not specified')}
🔧 *Technologies:* {escape_markdown(', '.join(offer['technologies']))}
🏠 *Work Modes:* {escape_markdown(', '.join(offer['work_modes']))}
📄 *Contract Types:* {escape_markdown(', '.join(offer['contract_types']))}
📍 *Location:* {escape_markdown(', '.join(offer['workplace']))}
🔗 [View Offer](https://it.pracuj.pl/praca/{offer['id']})
"""

def split_messages(offers, max_length=3000):  # Using 3000 to leave room for formatting
    messages = []
    current_message = "*🔥 New Job Offers Found\\!*\n"
    
    for offer in offers:
        offer_text = format_offer(offer) + "\n\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\n"
        
        # If adding this offer would exceed limit, start new message
        if len(current_message) + len(offer_text) > max_length:
            messages.append(current_message)
            current_message = "*🔥 More Job Offers\\!*\n" + offer_text
        else:
            current_message += offer_text
    
    if current_message:
        messages.append(current_message)
    
    return messages

def notify_new_offers(new_offers):
    if new_offers:
        messages = split_messages(new_offers)
        send_telegram_messages(messages)