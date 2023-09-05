from unittest import TestCase

from authors.forms import RegisterForm
from django.test import TestCase as DjangoTestCase
from django.urls import reverse
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
    def test_fields_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

# Teste que verifica se help_text corresponde aos campos
    @parameterized.expand([
        ('username', (
            'Obrigatório. 150 caracteres ou menos. '
            'Letras, números e @/./+/-/_ apenas.')),
        ('email', 'O e-mail deve ser válido.'),
        ('password', (
            'Senha deve ter pelo menos um caracter maiúsculo, '
            'um caracter minúsculo e um número. A senha deve '
            'possuir pelo menos 8 caracteres.')),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

# Teste que verifica se os labels correspondem aos campos
    @parameterized.expand([
        ('username', 'Nome do usuário'),
        ('first_name', 'Nome'),
        ('last_name', 'Sobrenome'),
        ('email', 'E-mail'),
        ('password', 'Digite sua senha'),
        ('password2', 'Confirme sua senha'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)

# Classe de teste de integração do form


class AuthorRegisterFormIntegrationTest(DjangoTestCase):

    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anyemail.com',
            'password': 'Str0ngP@ssword1',
            'password2': 'Str0ngP@ssword1',
        }
        return super().setUp(*args, **kwargs)

# Teste que verifica quando o campo está vazio
    @parameterized.expand([
        ('first_name', 'Este campo não pode estar vazio'),
        ('last_name', 'Este campo não pode estar vazio'),
        ('username', 'Este campo não pode estar vazio'),
        ('email', 'E-mail é obrigatório'),
        ('username', 'Este campo não pode estar vazio'),
        ('password', 'A senha não pode estar vazia'),
        ('password2', 'A senha não pode estar vazia'),

    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))
