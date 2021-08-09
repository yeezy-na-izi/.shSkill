from django.contrib.auth.forms import AuthenticationForm
from .models import Account


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = [
            'email',
            'password1',
        ]
