from authors.forms import RegisterForm
from django.test import TestCase
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    # testa se os placesholders dos campos estão ok
    @parameterized.expand([
        ('username', 'Digite seu nome de usuário'),
        ('email', 'Digite seu e-mail'),
        ('first_name', 'Digite seu primeiro nome'),
        ('last_name', 'Digite seu sobrenome'),
        ('password', 'Sua senha'),
        ('password2', 'Digite novamente sua senha'),
    ])
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)
