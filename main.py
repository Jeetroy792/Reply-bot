import os
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
    return "Bot is alive!"

def run_flask():
    # Koyeb এর জন্য পোর্ট ৮০০০ এ রান করা ভালো অথবা ড্যাশবোর্ড থেকে ৮০৮০ সেট করতে হবে
    app.run(host='0.0.0.0', port=8000) 

def start_flask():
    t = Thread(target=run_flask)
    t.start()

# 'bot_session' এর জায়গায় None দিলে Koyeb এ ফাইল রাইটিং এরর হবে না
bot = TelegramClient(None, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("<b>Welcome! 👋</b>\n\nThis bot is for <b>Direct Contact</b>. Send your message below.", parse_mode='html')

@bot.on(events.NewMessage)
async def handle_messages(event):
    # যদি মেসেজটি OWNER এর না হয় এবং কোনো কমান্ড না হয়
    if event.sender_id != OWNER_ID and not event.text.startswith('/'):
        # অ্যাডমিনকে মেসেজ পাঠানো
        user_info = f"<b>New Message from ID:</b> <code>{event.sender_id}</code>\n\n"
        await bot.send_message(OWNER_ID, user_info + event.text, parse_mode='html')
        await event.respond("<i>Message sent to admin!</i>", parse_mode='html')
    
    # যদি OWNER রিপ্লাই দেয়
    elif event.sender_id == OWNER_ID and event.is_reply:
        original_msg = await event.get_reply_message()
        try:
            # আইডি খুঁজে বের করার আরও শক্তিশালী লজিক
            parts = original_msg.text.split('ID: ')
            if len(parts) > 1:
                user_id_str = parts[1].split('\n')[0].strip()
                user_id = int(user_id_str)
                await bot.send_message(user_id, event.text)
                await event.respond(f"✅ Reply sent to {user_id}!")
            else:
                await event.respond("❌ Could not find user ID in the message.")
        except Exception as e:
            await event.respond(f"❌ Error: {str(e)}")

if __name__ == '__main__':
    start_flask()
    print("Bot is running...")
    bot.run_until_disconnected()
