from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
from lexicon.lexicon_ru import MESSAGE_TEXT, MESSAGE_VIDEO, MESSAGE_PAPER
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from keyboards.user_keyboards import *
from aiogram.types import CallbackQuery
from resources.links import LINK_VIDEO, ID_TG_IMAGE
import time
import asyncio
from aiogram import Bot

router = Router()


# состояния бота
class Form(StatesGroup):
    video1 = State()
    paper1 = State()
    video2 = State()
    paper2 = State()
    video3 = State()
    paper3 = State()


# Создаем "базу данных" пользователей
user_dict = {}
minutes = 60


# Этот handler срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext, bot: Bot) -> None:
    keyboard = web_app_keyboard()
    await message.answer(text=MESSAGE_TEXT['text0'],
                         reply_markup=keyboard)
    keyboard = see_video(cb='video1')
    await message.answer_photo(photo=ID_TG_IMAGE['image1'],
                               caption=MESSAGE_TEXT['text1'],
                               reply_markup=keyboard)
    await state.set_state(Form.video1)
    await asyncio.sleep(60 * minutes)
    await check_state_video('video1', message, state)


# нажата кнопка "Смотреть видео" и отправляется ссылка на первую статья
@router.callback_query(F.data == 'video1')
async def process_buttons_press(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(f"{LINK_VIDEO['video1']}{LINK_VIDEO['video1']}")
    time.sleep(5 * minutes)
    keyboard = read_paper(cb='paper1')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image2'],
                                        caption=MESSAGE_TEXT['text2'],
                                        reply_markup=keyboard)
    await state.set_state(Form.paper1)
    await asyncio.sleep(60 * minutes)
    await check_state_paper('paper1', callback.message, state)


# нажата кнопка "Читать статью" первую и отправлена ссылка на второе видео
@router.callback_query(F.data == 'paper1')
async def process_buttons_press(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(text="https://telegra.ph/Statya1-01-12")
    time.sleep(5 * minutes)
    keyboard = see_video(cb='video2')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image3'],
                                        caption=MESSAGE_TEXT['text3'],
                                        reply_markup=keyboard)
    await state.set_state(Form.video2)
    await asyncio.sleep(60 * minutes)
    await check_state_video('video2', callback.message, state)


# нажата кнопка "Смотреть видео" и отправляется ссылка на первую статья
@router.callback_query(F.data == 'video2')
async def process_buttons_press(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(f"{LINK_VIDEO['video2']}{LINK_VIDEO['video2']}")
    time.sleep(5 * minutes)
    keyboard = read_paper(cb='paper2')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image2'],
                                        caption=MESSAGE_TEXT['text55'],
                                        reply_markup=keyboard)
    await state.set_state(Form.paper2)
    await asyncio.sleep(60 * minutes)
    await check_state_paper('paper2', callback.message, state)


# нажата кнопка "Смотреть видео" второе и отправляется ссылка на третье видео
@router.callback_query(F.data == 'paper2')
async def process_buttons_press(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(text="https://telegra.ph/Statya2-01-12")
    time.sleep(6 * minutes)
    keyboard = see_video(cb='video3')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image4'],
                                        caption=MESSAGE_TEXT['text4'],
                                        reply_markup=keyboard)
    await state.set_state(Form.video3)
    await asyncio.sleep(60 * minutes)
    await check_state_video('video3', callback.message, state)


# нажата кнопка "Смотреть видео" третье и отправлена ссылка на вторую статью
@router.callback_query(F.data == 'video3')
async def process_buttons_press(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(f"{LINK_VIDEO['video3']}{LINK_VIDEO['video3']}")
    time.sleep(5 * minutes)
    keyboard = read_paper(cb='paper3')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image2'],
                                        caption=MESSAGE_TEXT['text5'],
                                        reply_markup=keyboard)
    await state.set_state(Form.paper3)
    await asyncio.sleep(60 * minutes)
    await check_state_paper('paper3', callback.message, state)


# нажата кнопка "Читать статью" вторую и отправляется ОФФЕР
@router.callback_query(F.data == 'paper3')
async def process_buttons_press(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.answer(text="https://telegra.ph/Ctatya-3-01-12")
    time.sleep(10 * minutes)
    await callback.message.answer(text=MESSAGE_TEXT['text6'])
    time.sleep(15 * minutes)
    keyboard = question1()
    await callback.message.answer(text=MESSAGE_TEXT['text7'],
                                  reply_markup=keyboard)
    await asyncio.sleep(15 * minutes)
    keyboard = finish()
    await callback.message.answer(text=MESSAGE_TEXT['text8'],
                                  reply_markup=keyboard)


# отправляем ответы
@router.callback_query(F.data.startswith('answer'))
async def process_buttons_press(callback: CallbackQuery) -> None:
    await callback.message.answer(f"{LINK_VIDEO[callback.data]}{LINK_VIDEO[callback.data]}")


# отправляем блок с вопросами
@router.callback_query(F.data == 'question')
async def process_buttons_press(callback: CallbackQuery) -> None:
    keyboard = question2()
    await callback.message.answer(text=MESSAGE_TEXT['text9'],
                                  reply_markup=keyboard)
    await asyncio.sleep(15 * minutes)
    keyboard = finish()
    await callback.message.answer(text=MESSAGE_TEXT['text8'],
                                  reply_markup=keyboard)

# отправляем блок
@router.callback_query(F.data == 'ok')
async def process_buttons_press(callback: CallbackQuery) -> None:
    await callback.message.answer(text=MESSAGE_TEXT['text10'])
    time.sleep(5 * minutes)
    await callback.message.answer(text=MESSAGE_TEXT['text11'])


async def check_state_video(chek_state: str, message: Message, state: FSMContext):
    current_state = await state.get_state()  # текущее машинное состояние пользователя

    if current_state == f'Form:{chek_state}':
        keyboard = see_video(chek_state)
        await message.answer_photo(photo=ID_TG_IMAGE['image6'],
                                   caption=MESSAGE_VIDEO['video1']+f'state: {current_state}',
                                   reply_markup=keyboard)
        await asyncio.sleep(20 * minutes)
        current_state = await state.get_state()
        if current_state == f'Form:{chek_state}':
            keyboard = see_video(chek_state)
            await message.answer_photo(photo=ID_TG_IMAGE['image7'],
                                       caption=MESSAGE_VIDEO['video2']+f'state: {current_state}',
                                       reply_markup=keyboard)
            await asyncio.sleep(30 * minutes)
            current_state = await state.get_state()
            if current_state == f'Form:{chek_state}':
                keyboard = see_video(chek_state)
                await message.answer(text=MESSAGE_VIDEO['video3']+f'state: {current_state}',
                                     reply_markup=keyboard)


async def check_state_paper(chek_state: str, message: Message, state: FSMContext):
    current_state = await state.get_state()  # текущее машинное состояние пользователя
    if current_state == f'Form:{chek_state}':
        keyboard = read_paper(chek_state)
        await message.answer_photo(photo=ID_TG_IMAGE['image6'],
                                   caption=MESSAGE_PAPER['paper1'],
                                   reply_markup=keyboard)
        await asyncio.sleep(20 * minutes)
        current_state = await state.get_state()
        if current_state == f'Form:{chek_state}':
            keyboard = read_paper(chek_state)
            await message.answer(text=MESSAGE_PAPER['paper2'],
                                 reply_markup=keyboard)
            await asyncio.sleep(30 * minutes)
            current_state = await state.get_state()
            if current_state == f'Form:{chek_state}':
                keyboard = read_paper(chek_state)
                await message.answer(text=MESSAGE_PAPER['paper3'],
                                     reply_markup=keyboard)
