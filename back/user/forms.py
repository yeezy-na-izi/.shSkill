from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Account


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = [
            'email',
            'password1',
        ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
