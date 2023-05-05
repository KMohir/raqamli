from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from db import db
from translation import _
def gender(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Erkak",lang)),
                KeyboardButton(text=_("Ayol", lang))
            ],


        ],
        resize_keyboard=True
    )
    return button

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
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Su'niy intelekt",lang)),


                KeyboardButton(text=_("Kiberxavsizlik", lang))
            ],

            [
                KeyboardButton(text=_("Tadbirkorlik va Moliya", lang)),
                KeyboardButton(text=_("O'yin sanoati", lang))
            ],

            [
                KeyboardButton(text=_("Boshqa", lang))
            ],
        ],
        resize_keyboard=True
    )
    return button
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
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Andijon viloyati",lang)),
                KeyboardButton(text=_("Buxoro viloyati", lang))
            ],

            [
                KeyboardButton(text=_("Fargʻona viloyati", lang)),
                KeyboardButton(text=_("Jizzax viloyati", lang))
            ],

            [
                KeyboardButton(text=_("Xorazm viloyati", lang)),
                KeyboardButton(text=_("Namangan viloyati", lang))
            ],
            [
                KeyboardButton(text=_("Navoiy viloyati", lang)),
                KeyboardButton(text=_("Qashqadaryo viloyati", lang))
            ],
            [
                KeyboardButton(text=_("Qoraqalpogʻiston Respublikasi", lang)),
                KeyboardButton(text=_("Samarqand viloyati", lang))
            ],
            [
                KeyboardButton(text=_("Sirdaryo viloyati", lang)),
                KeyboardButton(text=_("Surxondaryo viloyati", lang))
            ],
            [
                KeyboardButton(text=_("Toshkent viloyati", lang)),
                KeyboardButton(text=_("Toshkent shahri", lang))
            ],
        ],
        resize_keyboard=True
    )
    return button
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