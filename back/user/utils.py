from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return text_type(user.is_active) + text_type(user.username) + text_type(timestamp)


def return_correct_phone(phone):
    phone = str(phone)
    if phone:
        if phone[0] == '9':
            phone = '+7' + phone
        elif phone[0] == '8':
            phone = '+7' + phone[1:]
        elif phone[0] == '7':
            phone = '+' + phone
    return phone


token_generator = AppTokenGenerator()
