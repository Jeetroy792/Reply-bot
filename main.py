import os
from flask import Flask
from threading import Thread
from telethon import TelegramClient, events

# --- CONFIGURATION ---
API_ID = 24670806               # Replace with your API ID
API_HASH = '82134723a32b2cae76b9cfb3b1570745'     # Replace with your API HASH
BOT_TOKEN = '8246857362:AAH048LKLcdI_C3y_0RvLIA9qz2B3OrawvI'   # Replace with your Bot Token
OWNER_ID = 8229228616           # Replace with your Chat ID
# ---------------------

# Flask app to keep the bot alive on Koyeb
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def start_flask():
    t = Thread(target=run_flask)
    t.start()

# Telegram Bot Logic
bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("<b>Welcome! 👋</b>\n\nThis bot is for <b>Direct Contact</b>. Send your message below.", parse_mode='html')

@bot.on(events.NewMessage)
async def handle_messages(event):
    if event.sender_id != OWNER_ID and not event.text.startswith('/'):
        user_info = f"<b>New Message from ID:</b> <code>{event.sender_id}</code>\n\n"
        await bot.send_message(OWNER_ID, user_info + event.text, parse_mode='html')
        await event.respond("<i>Message sent to admin!</i>", parse_mode='html')
    
    elif event.sender_id == OWNER_ID and event.is_reply:
        original_msg = await event.get_reply_message()
        try:
            user_id = int(original_msg.text.split('\n')[0].split(': ')[1])
            await bot.send_message(user_id, event.text)
            await event.respond("✅ Reply sent!")
        except:
            await event.respond("❌ Error identifying user.")

if __name__ == '__main__':
    start_flask() # Starts the web server
    print("Bot is running...")
    bot.run_until_disconnected()
  
