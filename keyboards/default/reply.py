from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db import db
from translation import _
import requests
def gender(message):
    lang = db.get_lang(message.from_user.id)
    button = ReplyKeyboardMarkup()
    keyboard = InlineKeyboardMarkup(row_width=2)

    def get_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if status code is not 2xx
            data = response.json()  # Assuming the response is in JSON format
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

        # Example usage

    url = "https://raqamli-office.uz/api/form-request/details"  # Replace with your API endpoint URL
    data = get_data(url)

    if data:
        for key in range(len(data)):
            buttons = [
                InlineKeyboardButton(data['genders'][key]['translation']['value'], callback_data=data['genders'][key]['translation']['translatable_id']),

            ]

            keyboard.add(*buttons)

    return keyboard



def get_lang_for_button(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Ariza qoldirish",lang)
    )
            ],
            [
                KeyboardButton(text=_("Texnik yordamga habar yozish",lang)
    )
            ],
            [
                KeyboardButton(text=_("Tilni o'zgartirish",lang))
            ],
            [
                KeyboardButton(text=_("Raqamli Yordamchi haqida bilish", lang))
            ],

        ],
        resize_keyboard=True
    )
    return button
def direction(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup()
    keyboard = InlineKeyboardMarkup(row_width=2)


    def get_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if status code is not 2xx
            data = response.json()  # Assuming the response is in JSON format
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

        # Example usage
    url = "https://raqamli-office.uz/api/industries"  # Replace with your API endpoint URL
    data = get_data(url)
    if data:
        for key in range(len(data)):



            buttons = [
                InlineKeyboardButton(data[key]['translation']['value'], callback_data=data[key]['translation']['id']),


            ]

            keyboard.add(*buttons)





    return keyboard
def gmail(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("O'tkazib yuborish",lang)),
            ]],
        resize_keyboard=True
    )
    return button
def check(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Tasdiqlash",lang)),
            ],
        [
            KeyboardButton(text=_("Qayta toldirish", lang)),
        ]],
        resize_keyboard=True
    )
    return button
def region(message):
    lang = db.get_lang(message.from_user.id)
    button = ReplyKeyboardMarkup()
    keyboard = InlineKeyboardMarkup(row_width=2)

    def get_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if status code is not 2xx
            data = response.json()  # Assuming the response is in JSON format
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

        # Example usage

    url = "https://raqamli-office.uz/api/regions"  # Replace with your API endpoint URL
    data = get_data(url)
    if data:
        for key in range(len(data)):
            buttons = [
                InlineKeyboardButton(data[key]['translation']['value'], callback_data=data[key]['translation']['id']),

            ]

            keyboard.add(*buttons)

    return keyboard


# def get_project_for_user(message):
#     lang = db.get_lang(message.from_user.id)
#     button=ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text=_("Protestim",lang)
#     )
#             ],
#             [
#                 KeyboardButton(text=_("2 chi proyekt",lang))
#             ],
#             [
#                 KeyboardButton(text=_("3 chi proyekt",lang)
#     )
#             ],
#             [
#                 KeyboardButton(text=_("4 chi proyekt",lang))
#             ],
#
#         ],
#         resize_keyboard=True
#     )
#     return button


def change_lang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Русский язык")

            ],
            [
                KeyboardButton(text="O'zbek tili")
            ],

        ],
        resize_keyboard=True
    )
    return button
def changelang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Tilni o'zgartirish")

            ],

        ],
        resize_keyboard=True
    )
    return button
def key(lang):

    if lang=='uz':
        keyboardcontakt=ReplyKeyboardMarkup(

            keyboard=[[

                KeyboardButton(text="Kontakni yuborish",
                               request_contact=True

                               )
                ],

            ],resize_keyboard=True

        )
        return keyboardcontakt
    elif lang=='ru':
        keyboardcontakt=ReplyKeyboardMarkup(

            keyboard=[[

                KeyboardButton(text="Отправить контакт",
                               request_contact=True

                               )
                ],

            ],resize_keyboard=True

        )
        return keyboardcontakt