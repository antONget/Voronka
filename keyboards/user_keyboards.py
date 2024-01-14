from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo


def web_app_keyboard():
    web_app_btn = KeyboardButton(
        text='КУПИТЬ',
        web_app=WebAppInfo(url="https://xn--80agfmikluu.guru/inozemtsev")
    )
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[web_app_btn]],
        resize_keyboard=True
    )
    return keyboard


def see_video(cb):
    button = InlineKeyboardButton(
        text='СМОТРИ ВИДЕО',
        callback_data=cb
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button]]
    )
    return keyboard


def read_paper(cb):
    button = InlineKeyboardButton(
        text='ЧИТАЙ СТАТЬЮ',
        callback_data=cb
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button]]
    )
    return keyboard


def question1():
    button1 = InlineKeyboardButton(
        text='1',
        callback_data='answer1'
    )
    button2 = InlineKeyboardButton(
        text='2',
        callback_data='answer2'
    )
    button3 = InlineKeyboardButton(
        text='3',
        callback_data='answer3'
    )
    button4 = InlineKeyboardButton(
        text='4',
        callback_data='answer4'
    )
    button5 = InlineKeyboardButton(
        text='5',
        callback_data='answer5'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1, button2, button3],[button4, button5]]
    )
    return keyboard


def question2():
    button1 = InlineKeyboardButton(
        text='1',
        callback_data='answer1'
    )
    button2 = InlineKeyboardButton(
        text='2',
        callback_data='answer2'
    )
    button3 = InlineKeyboardButton(
        text='3',
        callback_data='answer3'
    )
    button4 = InlineKeyboardButton(
        text='4',
        callback_data='answer4'
    )
    button5 = InlineKeyboardButton(
        text='5',
        callback_data='answer5'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1, button2, button3, button4, button5]]
    )
    return keyboard

def finish():
    button1 = InlineKeyboardButton(
        text='Вопросов нет. Я вписываюсь',
        callback_data='ok'
    )
    button2 = InlineKeyboardButton(
        text='Еще вопросик',
        callback_data='question'
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1, button2]]
    )
    return keyboard