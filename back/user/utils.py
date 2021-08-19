from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages
from six import text_type

import re


class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return text_type(user.is_active) + text_type(user.username) + text_type(timestamp)


def return_correct_phone(phone: str):
    clearPhone = "".join(re.findall(r"[\+0-9]", phone))

    if clearPhone:
        clearPhone = clearPhone[0] + clearPhone[1:].replace("+", "")
        if clearPhone[0] == '9':
            clearPhone = '+7' + clearPhone
        elif phone[0] == '8':
            clearPhone = '+7' + clearPhone[1:]
        elif clearPhone[0] == '7':
            clearPhone = '+' + clearPhone
    return clearPhone


def is_correctly_email(email: str):
    correctMail = re.findall(r"[\w\.]+@\w+\.\w+", email)
    if not correctMail:
        return False
    return True


token_generator = AppTokenGenerator()
