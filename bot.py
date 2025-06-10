import telebot
from config import TELEGRAM_BOT_TOKEN
from flask import Flask, render_template_string
import threading

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template_string("""
        <html>
        <head><title>Trading Bot Dashboard</title></head>
        <body>
            <h1>Telegram Trading Smart Bot Dashboard</h1>
            <p>Status: Running</p>
            <p>Available commands: /buy, /sell, /balance</p>
        </body>
        </html>
    """)

def run_dashboard():
    app.run(port=8080)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Telegram Trading Smart Bot!")

if __name__ == "__main__":
    threading.Thread(target=run_dashboard, daemon=True).start()
    print("Dashboard running at http://localhost:8080")
    print("Bot is running...")
    bot.polling()
