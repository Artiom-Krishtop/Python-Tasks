import os
from sqlalchemy import URL
from engine import Engine
from connection import Connection
from telebot import TeleBot
from dotenv import load_dotenv
from models import UsersORM, PushupsORM

load_dotenv()

url_object = URL.create(
    "postgresql+psycopg2",
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

connection_object = Connection(Engine(url_object).create_engine())
connection = connection_object.get_connection()

bot = TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.send_message(message.chat.id, message)
    except Exception as e:    
        bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['statistic'])
def statistic(message):
    bot.send_message(message.chat.id, 'Статистика')

bot.polling(none_stop=True)
