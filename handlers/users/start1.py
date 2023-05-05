from email._header_value_parser import ContentType
from io import BytesIO

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode, Message, ReplyKeyboardRemove
from aiogram.types import InputFile
from db import db
from keyboards.default.reply import key, get_lang_for_button, direction, region, gender, gmail, check
from keyboards.inline.support import langMenu, support_keyboard
from loader import dp, bot

# from keyboards.default.reply import get_lang_for_button, get_project_for_user
from states.state import answer, questions, ariza
from translation import _

global lang

@dp.message_handler(text='/apply')
@dp.message_handler(text='Ariza qoldirish')
@dp.message_handler(text='Оставить заявку')
async def set_lang(message: types.Message):
    lang = db.get_lang(message.from_user.id)
    await bot.send_message(message.from_user.id, _("Ism  kiriting",lang),reply_markup=ReplyKeyboardRemove())
    await ariza.name.set()

@dp.message_handler(state=ariza.name)
async def set_lang(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    name = message.text
    async with state.proxy() as data:

        data['name'] = name

    await bot.send_message(message.from_user.id, _("Familiyangizni kiriting",lang))
    await ariza.fename.set()

@dp.message_handler(state=ariza.fename)
async def register_command_handler(message: types.Message, state: FSMContext):
    fename=message.text
    lang = db.get_lang(message.from_user.id)

    async with state.proxy() as data:

        data['fename'] = fename

    await bot.send_message(message.from_user.id, _("Elektron pochta manzilingizni kiriting (shart emas)", lang),
                           reply_markup=gmail(message))
    await ariza.email.set()

@dp.message_handler(state=ariza.email)
async def register_command_handler(message: types.Message, state: FSMContext):
    email=message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:

        data['email'] = email

    await message.answer(_("Telefon raqamingizni kiriting",lang),reply_markup=key(lang))
    await ariza.phone.set()

@dp.message_handler(state=ariza.phone, content_types=types.ContentType.TEXT)
async def process_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = db.get_lang(message.from_user.id)
    contact =message.text
    if contact[0:4]=='+998':
        phone=message.text
        async with state.proxy() as data:

            data['phone'] = phone

        await message.answer(_("Yo'nalishni tanlang", lang), reply_markup=direction(message))

        await ariza.direction.set()

    else:
        await message.answer(_("Telefon raqam noto'g'ri kiritildi, iltimos telefon raqamni +998XXXXXXXX formatda kiriting yoki 'Kontakni yuborish' tugmasiga bosing.",lang),reply_markup=key(lang))
        await ariza.phone.set()


@dp.message_handler(state=ariza.phone, content_types=types.ContentType.CONTACT)
async def process_name(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    contact = str(message.contact.phone_number)
    async with state.proxy() as data:
        data['phone'] = contact

    await message.answer(_("Yo'nalishni tanlang",lang), reply_markup=direction(message))


    await ariza.direction.set()


@dp.message_handler(text=["Boshqa","Другой"],state=ariza.direction)
async def process_name(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await bot.send_message(message.from_user.id, _("Yo'nalishni yozing",lang),reply_markup=ReplyKeyboardRemove())
    await ariza.directiontwo.set()

@dp.message_handler(state=ariza.directiontwo)
async def process_name(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    direction=message.text
    async with state.proxy() as data:
        data['direction'] = direction
    await bot.send_message(message.from_user.id,_('Hududni tanlang',lang),reply_markup=region(message))
    await ariza.Region.set()
@dp.message_handler(text=["Su'niy intelekt","Kiberxavsizlik","Tadbirkorlik va Moliya","O'yin sanoati",
                          "Искусственный интеллект","Кибербезопасность","Предпринимательство и финансы","Игровая индустрия","Другой"],state=ariza.direction)
async def process_name(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    direction=message.text
    async with state.proxy() as data:
        data['direction'] = direction
    await bot.send_message(message.from_user.id,_('Hududni tanlang',lang),reply_markup=region(message))
    await ariza.Region.set()
@dp.message_handler(state=ariza.direction)
async def process_name(message: Message, state: FSMContext):
    await message.answer("Yo'nalishni tanlang", reply_markup=direction(message))
    await ariza.direction.set()
@dp.message_handler(state=ariza.direction)
async def process_name(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    direction=message.text
    async with state.proxy() as data:
        data['direction'] = direction
    await bot.send_message(message.from_user.id,_('Hududni tanlang',lang),reply_markup=region(message))
    await ariza.Region.set()
@dp.message_handler(text=["Andijon viloyati","Buxoro viloyati","Fargʻona viloyati","Jizzax viloyati","Xorazm viloyati","Namangan viloyati","Navoiy viloyati",
"Qashqadaryo viloyati","Qoraqalpogʻiston Respublikasi","Samarqand viloyati","Sirdaryo viloyati","Surxondaryo viloyati","Toshkent viloyati","Toshkent shahri"],state=ariza.Region)
async def process_name(message: Message, state: FSMContext):

    lang = db.get_lang(message.from_user.id)
    regiontext=message.text
    async with state.proxy() as data:
        data['region'] = regiontext

    await message.answer(_("Jinsi",lang), reply_markup=gender(message))


    await ariza.gender.set()

@dp.message_handler(text=['Erkak','Ayol',"Мужчина","Женщина"],state=ariza.gender)
async def process_name(message: Message, state: FSMContext):

    lang = db.get_lang(message.from_user.id)
    gender=message.text
    async with state.proxy() as data:
        data['gender'] = gender

    await message.answer(_("Oʻzingiz haqizda aytib bering",lang), reply_markup=ReplyKeyboardRemove())


    await ariza.about.set()
@dp.message_handler(state=ariza.gender)
async def process_name(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Jinsi",lang), reply_markup=gender(message))


    await ariza.gender.set()
@dp.message_handler(state=ariza.about)
async def process_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = db.get_lang(message.from_user.id)
    about=message.text
    async with state.proxy() as data:
        data['about'] = about
    file_path = "doc/15-04-2023.docx"  # Replace with the actual path to your file
    with open(file_path, "rb") as f:
        byte_stream = BytesIO(f.read())

    input_file = InputFile(byte_stream, filename=_("Anketa_shabloni.docx",lang))
    caption = _("Yuqoridagi shablonni yuklab oling, uni toʻldiring va shu yerga yuklang",lang)

    message = await bot.send_document(message.from_user.id, input_file, caption=caption)

    byte_stream.close()
    await ariza.document.set()

@dp.message_handler(state=ariza.document,content_types=['document'])
async def process_name(message: Message, state: FSMContext):

    all_data = await state.get_data()
    lang = db.get_lang(message.from_user.id)
    name=all_data['name']
    fename=all_data['fename']
    email=all_data['email']
    phone=all_data['phone']
    direction=all_data['direction']
    region=all_data['region']
    gender=all_data['gender']
    about=all_data['about']
    if email =="O'tkazib yuborish" or email=="Пропустить":
        email ="Email kiritilmadi "
    if lang=='uz':
        text=f"""Ism:{name}\nFamiliya: {fename}\nEmail: {email}\nTelephone: {phone}\nYo'nalish: {direction}\nYashash joyi: {region}\nJinsi: {gender}\nO'zi haqida: {about}"""
    else:
            text = f"""Имя:{name}\nФамилия: {fename}\nEmail: {email}\nTelephone: {phone}\nНаправление: {direction}\nСреда обитания: {region}\nПол: {gender}\nО себе: {about}"""


    await message.copy_to(message.from_user.id,caption=text,reply_markup=check(message))
    await ariza.check.set()
@dp.message_handler(state=ariza.document,content_types = ['text', 'audio', 'photo', 'sticker', 'video', 'video_note', 'voice', 'contact', 'location', 'venue', 'poll', 'dice', 'game', 'invoice', 'successful_payment', 'passport_data', 'animation', 'passport_file', 'proxi', 'message_auto_delete_timer_changed'])
async def process_name(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Word file ni yuboring",lang))

    await ariza.document.set()


@dp.message_handler(state=ariza.check,text=['Tasdiqlash','Qayta toldirish','Подтвердить','Занаво пополнить'])
async def check_data(message: Message, state: FSMContext):
    all_data = await state.get_data()
    lang = db.get_lang(message.from_user.id)
    name=all_data['name']
    fename=all_data['fename']
    email=all_data['email']
    phone=all_data['phone']
    direction=all_data['direction']
    region=all_data['region']
    gender=all_data['gender']
    about=all_data['about']
    if email =="O'tkazib yuborish" or email=="Пропустить":
        email ="Email kiritilmadi"

    text=f"""Ism:{name}\nFamiliya: {fename}\nEmail: {email}\nTelephone: {phone}\nYo'nalish: {direction}\nYashash joyi: {region}\nJinsi: {gender}\nO'zi haqida: {about}"""


    if message.text=='Tasdiqlash'or message.text=='Подтвердить':
        await message.copy_to(-1001972594621, caption=text)
        await message.answer(_("Tabriklaymiz, sizni arizangiz yuborildi! 🎉", lang), reply_markup=get_lang_for_button(message))
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, _("Ism  kiriting", lang), reply_markup=ReplyKeyboardRemove())
        await ariza.name.set()