import os
import re
from flask import Flask
from threading import Thread
from telethon import TelegramClient, events

# --- CONFIGURATION ---
API_ID = 24670806               
API_HASH = '82134723a32b2cae76b9cfb3b1570745'     
BOT_TOKEN = '8246857362:AAH048LKLcdI_C3y_0RvLIA9qz2B3OrawvI'   
OWNER_ID = 8229228616           
# ---------------------

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive and running!"

def run_flask():
    # Using port 8000 for Koyeb health checks
    app.run(host='0.0.0.0', port=8000)

def start_flask():
    t = Thread(target=run_flask)
    t.start()

# Starting the bot without a local session file to prevent errors on cloud hosting
bot = TelegramClient(None, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    if event.sender_id != OWNER_ID:
        await event.respond
