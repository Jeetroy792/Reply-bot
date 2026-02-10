# Telegram Contact Bot (No-Ads)

A simple and lightweight Telegram Contact Bot built using **Telethon** and **Flask**. This bot allows users to message you directly through the bot, and you can reply to them by simply replying to the forwarded message. 

It is designed to be hosted on **Koyeb** or **Heroku** with zero advertisements.

## ✨ Features
- **No Ads:** Unlike Livegram, this bot is 100% private and ad-free.
- **Direct Contact:** Users can reach you without knowing your personal account.
- **Easy Reply:** Admin can reply to users directly by replying to the bot's message.
- **Koyeb Ready:** Includes a Flask server for health checks to keep the bot alive 24/7.

## 🛠️ Setup Instructions

1. **Get Telegram Credentials:**
   - Obtain your `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).
   - Get your `BOT_TOKEN` from [@BotFather](https://t.me/BotFather).
   - Get your `OWNER_ID` from [@userinfobot](https://t.me/userinfobot).

2. **Configure the Code:**
   - Open `main.py` and replace the placeholders with your actual credentials.

3. **Required Files:**
   - `main.py`: The main bot script.
   - `requirements.txt`: List of dependencies (`telethon`, `flask`).
   - `Procfile`: Command to run the bot on the server.

## 🚀 Deployment on Koyeb

1. Create a new account on [Koyeb](https://www.koyeb.com/).
2. Create a new Service and connect your GitHub repository.
3. Ensure your repository is **Private** to protect your credentials.
4. Set the following:
   - **Port:** 8080
   - **Protocol:** HTTP
5. Deploy! Your bot will be online.

## ⚠️ Privacy Warning
Always keep your repository **Private** if you are hardcoding your `API_ID`, `API_HASH`, and `BOT_TOKEN` inside `main.py`.
