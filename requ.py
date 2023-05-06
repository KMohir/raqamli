import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# def get_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception if status code is not 2xx
#         data = response.json()  # Assuming the response is in JSON format
#         return data
#     except requests.exceptions.RequestException as e:
#         print(f"Error occurred: {e}")
#         return None
#
# # Example usage
# url = "https://raqamli-office.uz/api/industries"  # Replace with your API endpoint URL
# data = get_data(url)
# if data:
#     for key in range(len(data)):
#         print(data[key]['translation']['id'],data[key]['translation']['value'])
#
# # import requests
# #
# # def submit_form():
# #     url = "https://raqamli-office.uz/api/form-request"  # Replace with your API endpoint URL
# #
# #     # Fill in the field values
# #     data = {
# #         "_name": "John",
# #         "l_name": "Doe",
# #         "project": "My Project",
# #         "gender_id": 1,
# #         "region_id": 2,
# #         "industry_id": 3,
# #         "another_industry": "Another Industry",
# #         "phone_number": "1234567890",
# #         "email": "john.doe@example.com",
# #         "about": "About me",
# #     }
# #     test_file = open("document.docx", "rb")
# #
# #     # Attach file
# #     files = {
# #         "file": test_file
# #     }
# #
# #     try:
# #         response = requests.post(url, data=data, files=files)
# #         response.raise_for_status()
# #         print("Status_code:",response.status_code)# Raise an exception if status code is not 2xx
# #         print("Form submitted successfully.")
# #     except requests.exceptions.RequestException as e:
# #         print(f"Error occurred: {e}")
# #
# # # Example usage
# # submit_form()

def gender():

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
    print('111111111111',data['genders'][0])
    # if data:
    #     for key in range(len(data)):
    #         buttons = [
    #             InlineKeyboardButton(data[key]['translatable_type']['value'], callback_data=data[key]['translatable_type']['translatable_id']),
    #
    #         ]
    #
    #         keyboard.add(*buttons)

    return keyboard
gender()