from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
from lexicon.lexicon_ru import MESSAGE_TEXT, MESSAGE_VIDEO, MESSAGE_PAPER, MESSAGE_ANSWER, MESSAGE_GREETING
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from keyboards.user_keyboards import *
from aiogram.types import CallbackQuery
from resources.links import LINK_VIDEO, ID_TG_IMAGE
import time
import asyncio
from aiogram import Bot
import logging

router = Router()


# состояния бота
class Form(StatesGroup):
    video1 = State()
    paper1 = State()
    video2 = State()
    paper2 = State()
    video3 = State()
    paper3 = State()
    finish = State()


# Создаем "базу данных" пользователей
user_dict = {}
minutes = 2


# Этот handler срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext) -> None:
    logging.info(f'process_start_command: {message.chat.id}')
    if message.from_user.first_name != None:
        hi = f'{message.from_user.first_name}, хай! '
    else:
        hi = ''
    keyboard = web_app_keyboard()
    await message.answer(text=hi+MESSAGE_TEXT['text0'],
                         reply_markup=keyboard)
    await message.answer(text=MESSAGE_GREETING['greet1'])

    # keyboard = see_video(cb='video1')
    # await message.answer_photo(photo=ID_TG_IMAGE['image1'],
    #                            caption=MESSAGE_TEXT['text1'],
    #                            reply_markup=keyboard)
    # await state.set_state(Form.video1)
    # await asyncio.sleep(60 * minutes)
    # await check_state_video('video1', message, state)


# нажата кнопка "Смотреть видео" и отправляется ссылка на первую статья
# @router.callback_query(F.data == 'video1')
# async def process_buttons_press_video1(callback: CallbackQuery, state: FSMContext) -> None:
#     logging.info(f'process_buttons_press_video1: {callback.message.chat.id}')
#     await callback.message.answer(f"{LINK_VIDEO['video1']}{LINK_VIDEO['video1']}")
    await asyncio.sleep(5 * minutes)  # 5
    keyboard = read_paper(cb='paper1')
    # keyboard = read_paper_link()
    await message.answer_photo(photo=ID_TG_IMAGE['image2'],
                               caption=MESSAGE_TEXT['text2'],
                               reply_markup=keyboard)
    await state.set_state(Form.paper1)
    await asyncio.sleep(60 * minutes)  # 60
    logging.info(f'process_buttons_press_video1: {message.chat.id},'
                 f' check_state_paper: {await state.get_state()}')
    await check_state_paper('paper1', message, state)


# нажата кнопка "Читать статью" первую и отправлена ссылка на второе видео
@router.callback_query(F.data == 'paper1')
async def process_buttons_press_paper1(callback: CallbackQuery, state: FSMContext) -> None:
    logging.info(f'process_buttons_press_paper1: {callback.message.chat.id}')
    await callback.message.answer(text="https://salebot.site/md/4636ea9ee9de29dbe0c397eba4845347")
    await asyncio.sleep(5 * minutes)  # 5
    keyboard = see_video(cb='video2')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image3'],
                                        caption=MESSAGE_TEXT['text3'],
                                        reply_markup=keyboard)
    await state.set_state(Form.video2)
    await asyncio.sleep(60 * minutes)  # 60
    logging.info(f'process_buttons_press_paper1: {callback.message.chat.id},'
                 f' check_state_video: {await state.get_state()}')
    await check_state_video('video2', callback.message, state)


# нажата кнопка "Смотреть видео" и отправляется ссылка на первую статья
@router.callback_query(F.data == 'video2')
async def process_buttons_press_video2(callback: CallbackQuery, state: FSMContext) -> None:
    logging.info(f'process_buttons_press_video2: {callback.message.chat.id}')
    await callback.message.answer(f"{LINK_VIDEO['video2']}{LINK_VIDEO['video2']}")
    await asyncio.sleep(5 * minutes)  # 5
    keyboard = read_paper(cb='paper2')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image2'],
                                        caption=MESSAGE_TEXT['text55'],
                                        reply_markup=keyboard)
    await state.set_state(Form.paper2)
    await asyncio.sleep(60 * minutes)  # 60
    logging.info(f'process_buttons_press_video2: {callback.message.chat.id},'
                 f' check_state_paper: {await state.get_state()}')
    await check_state_paper('paper2', callback.message, state)


# нажата кнопка "Смотреть видео" второе и отправляется ссылка на третье видео
@router.callback_query(F.data == 'paper2')
async def process_buttons_press_paper2(callback: CallbackQuery, state: FSMContext) -> None:
    logging.info(f'process_buttons_press_paper2: {callback.message.chat.id}')
    await callback.message.answer(text="https://salebot.site/md/46e75406a82b897a21766243965ba569")
    await asyncio.sleep(6 * minutes)  # 6
    keyboard = see_video(cb='video3')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image4'],
                                        caption=MESSAGE_TEXT['text4'],
                                        reply_markup=keyboard)
    await state.set_state(Form.video3)
    await asyncio.sleep(60 * minutes)  # 60
    logging.info(f'process_buttons_press_paper2: {callback.message.chat.id},'
                 f' check_state_video: {await state.get_state()}')
    await check_state_video('video3', callback.message, state)


# нажата кнопка "Смотреть видео" третье и отправлена ссылка на вторую статью
@router.callback_query(F.data == 'video3')
async def process_buttons_press_video3(callback: CallbackQuery, state: FSMContext) -> None:
    logging.info(f'process_buttons_press_video3: {callback.message.chat.id}')
    await callback.message.answer(f"{LINK_VIDEO['video3']}{LINK_VIDEO['video3']}")
    await asyncio.sleep(5 * minutes)  # 5
    keyboard = read_paper(cb='paper3')
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image2'],
                                        caption=MESSAGE_TEXT['text5'],
                                        reply_markup=keyboard)
    await state.set_state(Form.paper3)
    await asyncio.sleep(60 * minutes)  # 60
    logging.info(f'process_buttons_press_video3: {callback.message.chat.id},'
                 f' check_state_paper: {await state.get_state()}')
    await check_state_paper('paper3', callback.message, state)


# нажата кнопка "Читать статью" вторую и отправляется ОФФЕР
@router.callback_query(F.data == 'paper3')
async def process_buttons_press_paper3(callback: CallbackQuery, state: FSMContext) -> None:
    logging.info(f'process_buttons_press_paper3: {callback.message.chat.id}')
    await state.set_state(Form.finish)
    await callback.message.answer(text="https://salebot.site/md/2c13eaf6796abdd666c9539923d76dc1")
    await asyncio.sleep(10 * minutes)  # 10
    if await state.get_state() == f'Form:finish':
        keyboard = programm()
        await callback.message.answer(text=MESSAGE_TEXT['text6'],
                                      reply_markup=keyboard)
    await asyncio.sleep(15 * minutes)  # 15
    if await state.get_state() == f'Form:finish':
        keyboard = question1()
        await callback.message.answer(text=MESSAGE_TEXT['text7'],
                                      reply_markup=keyboard)
    await asyncio.sleep(15 * minutes)  # 15
    if await state.get_state() == f'Form:finish':
        keyboard = finish()
        await callback.message.answer(text=MESSAGE_TEXT['text8'],
                                      reply_markup=keyboard)


# отправляем ответы
@router.callback_query(F.data.startswith('answer'))
async def process_buttons_press_answer(callback: CallbackQuery) -> None:
    logging.info(f'process_buttons_press_answer: {callback.message.chat.id}')
    await callback.message.answer(text=MESSAGE_ANSWER[callback.data])
    # await callback.message.answer(f"{LINK_VIDEO[callback.data]}{LINK_VIDEO[callback.data]}")


# отправляем блок с вопросами
@router.callback_query(F.data == 'question')
async def process_buttons_press_question(callback: CallbackQuery, state: FSMContext) -> None:
    logging.info(f'process_buttons_press_question: {callback.message.chat.id}')
    keyboard = question2()
    await callback.message.answer_photo(photo=ID_TG_IMAGE['image5'],
                                        caption=MESSAGE_TEXT['text9'],
                                        reply_markup=keyboard)
    if await state.get_state() == f'Form:finish':
        await asyncio.sleep(15 * minutes)  # 15
        keyboard = finish()
        await callback.message.answer(text=MESSAGE_TEXT['text8'],
                                      reply_markup=keyboard)


# отправляем блок
@router.callback_query(F.data == 'ok')
async def process_buttons_press_ok(callback: CallbackQuery) -> None:
    logging.info(f'process_buttons_press_ok: {callback.message.chat.id}')
    await callback.message.answer(text=MESSAGE_TEXT['text10'])


async def check_state_video(chek_state: str, message: Message, state: FSMContext):
    current_state = await state.get_state()  # текущее машинное состояние пользователя
    if current_state == f'Form:{chek_state}':
        logging.info(f'check1_state_video-{chek_state}: {message.chat.id}')
        keyboard = see_video(chek_state)
        await message.answer_photo(photo=ID_TG_IMAGE['image6'],
                                   caption=MESSAGE_VIDEO['video1'],
                                   reply_markup=keyboard)
        await asyncio.sleep(20 * minutes)  # 20
        current_state = await state.get_state()
        if current_state == f'Form:{chek_state}':
            logging.info(f'check2_state_video-{chek_state}: {message.chat.id}')
            keyboard = see_video(chek_state)
            await message.answer_photo(photo=ID_TG_IMAGE['image7'],
                                       caption=MESSAGE_VIDEO['video2'],
                                       reply_markup=keyboard)
            await asyncio.sleep(30 * minutes)  # 30
            current_state = await state.get_state()
            if current_state == f'Form:{chek_state}':
                logging.info(f'check3_state_video-{chek_state}: {message.chat.id}')
                keyboard = see_video(chek_state)
                await message.answer(text=MESSAGE_VIDEO['video3'],
                                     reply_markup=keyboard)


async def check_state_paper(chek_state: str, message: Message, state: FSMContext):
    current_state = await state.get_state()  # текущее машинное состояние пользователя
    if current_state == f'Form:{chek_state}':
        logging.info(f'check1_state_papper-{chek_state}: {message.chat.id}')
        keyboard = read_paper(chek_state)
        await message.answer_photo(photo=ID_TG_IMAGE['image6'],
                                   caption=MESSAGE_PAPER['paper1'],
                                   reply_markup=keyboard)
        await asyncio.sleep(20 * minutes)  # 20
        current_state = await state.get_state()
        if current_state == f'Form:{chek_state}':
            logging.info(f'check2_state_papper-{chek_state}: {message.chat.id}')
            keyboard = read_paper(chek_state)
            await message.answer(text=MESSAGE_PAPER['paper2'],
                                 reply_markup=keyboard)
            await asyncio.sleep(30 * minutes)  # 30
            current_state = await state.get_state()
            if current_state == f'Form:{chek_state}':
                logging.info(f'check3_state_papper-{chek_state}: {message.chat.id}')
                keyboard = read_paper(chek_state)
                await message.answer(text=MESSAGE_PAPER['paper3'],
                                     reply_markup=keyboard)
