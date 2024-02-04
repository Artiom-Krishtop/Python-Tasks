import os
from sqlalchemy import URL
from engine import Engine
from session import Session
from telebot import TeleBot, types
from dotenv import load_dotenv
from models import UsersORM, PushupsORM, Base
from exceptions import ProcessBotException

load_dotenv()

url_object = URL.create(
    "postgresql+psycopg2",
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

engine_object = Engine(url_object)
engine = engine_object.create_engine()

session_object = Session(engine)
session = session_object.get_session()

Base.metadata.create_all(engine)

def tg_user_exists(id):
    return session.query(UsersORM.id).filter(UsersORM.tg_id == id).first() != None

def get_user_id(id):
    return session.query(UsersORM.id).filter(UsersORM.tg_id == id).scalar()

bot = TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

bot.set_my_commands(
    commands=[
        types.BotCommand('start', 'Start bot'),
        types.BotCommand('pushups', 'Enter your pushups'),
        types.BotCommand('statistic', 'Get my statistic'),
        types.BotCommand('help', 'Help')
    ],
    scope=types.BotCommandScopeChat(bot.get_me().id)
)

@bot.message_handler(commands=['start'])
def start(message):
    try:
        if not tg_user_exists(message.from_user.id):
            session.add(UsersORM(tg_id = message.from_user.id))
            session.commit()

        pushups_button = types.KeyboardButton('/pushups')
        statistic_button = types.KeyboardButton('/statistic')

        # pushups_button.add(types.KeyboardButton('/pushups'))
        # statistic_button.add(types.KeyboardButton('/statistic'))

        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        keyboard.add(pushups_button, statistic_button)

        bot.send_message(message.chat.id, f'Hello { message.from_user.first_name } { message.from_user.last_name }', reply_markup=keyboard)

    finally:
        session.rollback()
        session.close()

@bot.message_handler(commands=['pushups'])
def pushups(message):
    try:
        if not tg_user_exists(message.from_user.id):
            session.add(UsersORM(tg_id = message.from_user.id))
            session.commit()

        bot.send_message(message.chat.id, 'Enter your result:')
        bot.register_next_step_handler(message, add_result)
    finally:
        session.rollback()
        session.close()

def add_result(message):
    try:
        if not tg_user_exists(message.from_user.id):
            raise Exception('User not found!')

        result = message.text

        if result.isdigit():
            session.add(PushupsORM(user_id = get_user_id(message.from_user.id), number = result))
            session.commit()

            bot.send_message(message.chat.id, 'Great, your result has been added!')
        else:
            raise ProcessBotException('Enter valid value, please!')
    except ProcessBotException as e:
        bot.send_message(message.chat.id, e)
        bot.send_message(message.chat.id, 'Try again:')
        bot.register_next_step_handler(message, add_result)
    finally:
        session.rollback()
        session.close()

@bot.message_handler(commands=['statistic'])
def statistic(message):
    try:
        if not tg_user_exists(message.from_user.id):
            raise ProcessBotException('No results!')

        response_msg = ''

        results = session.query(PushupsORM).filter(PushupsORM.user_id == get_user_id(message.from_user.id)).all()
        
        for result in results:
            response_msg += 'Date: ' + result.created_at.strftime("%Y/%m/%d %H:%M") + '\nResult: ' + str(result.number)
            response_msg += '\n____________________'

        if(len(response_msg) == 0):
            response_msg = 'No resultes!'

        bot.send_message(message.chat.id, response_msg)
    except ProcessBotException as e:
        bot.send_message(message.chat.id, e)
    finally:
        session.rollback()
        session.close()

@bot.message_handler(commands=['help'])
def help(message):
    response_msg = ''

    response_msg += f'Hello { message.from_user.first_name } { message.from_user.last_name }'
    response_msg += '\n'
    response_msg += '\n'
    response_msg += 'Commands:\n'
    response_msg += '/start - Start bot\n'
    response_msg += '/pushups - Enter your pushups\n'
    response_msg += '/statistic - Get my statistic\n'

    bot.send_message(message.chat.id, response_msg)

@bot.message_handler()
def default(message):
    help(message)

bot.polling(none_stop=True)
