# src/setup_telegram.py
from telegram import Bot
import asyncio
import json

async def setup_telegram():
    # Load config
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    bot = Bot(token=config['telegram']['token'])
    
    try:
        # Get bot info
        me = await bot.get_me()
        print(f"Bot Info:\nName: {me.first_name}\nUsername: @{me.username}")
        
        # Get updates to see available chats
        updates = await bot.get_updates()
        if not updates:
            print("\nNo recent updates found. Please:")
            print("1. Open Telegram")
            print("2. Find your bot: @" + me.username)
            print("3. Send /start command to the bot")
            print("4. Run this script again")
            return
        
        print("\nAvailable Chats:")
        for update in updates:
            if update.message:
                chat = update.message.chat
                print(f"\nChat Type: {chat.type}")
                print(f"Chat ID: {chat.id}")
                print(f"Chat Username: {chat.username or 'N/A'}")
                print(f"Chat Title: {getattr(chat, 'title', 'N/A')}")
                
                # Try sending test message
                try:
                    await bot.send_message(
                        chat_id=chat.id,
                        text="Test message - setup successful!"
                    )
                    print("✓ Test message sent successfully")
                    
                    # Update config with working chat_id
                    config['telegram']['chat_id'] = str(chat.id)
                    with open('config.json', 'w') as f:
                        json.dump(config, f, indent=2)
                    print("✓ Config updated with working chat_id")
                    
                except Exception as e:
                    print(f"✗ Failed to send message: {str(e)}")
        
    except Exception as e:
        print(f"Setup Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(setup_telegram())