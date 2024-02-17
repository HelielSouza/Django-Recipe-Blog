### Receitas.com

## Português (pt-br)
Este é um projeto de um blog de receitas desenvolvido em Django, onde os usuários podem se cadastrar, publicar suas próprias receitas, editar e visualizar as receitas de outros usuários.

# Funcionalidades Principais:

Cadastro de Usuário: Os usuários podem se cadastrar no site para criar e gerenciar suas próprias receitas.
Publicação de Receitas: Os usuários podem publicar suas receitas, incluindo título, ingredientes, instruções e uma imagem ilustrativa.
Edição de Receitas: Os autores das receitas podem editar ou excluir suas próprias receitas a qualquer momento.
Visualização de Receitas: Os usuários podem visualizar receitas de outros usuários, incluindo detalhes como ingredientes, instruções e imagem.


Tecnologias Utilizadas:

- Django
- HTML/CSS
- JavaScript
- Banco de dados SQLite (por padrão, pode ser alterado para outros bancos de dados suportados pelo Django)

Instalação e Execução:

- Clone este repositório: git clone <URL_do_repositório>
- Crie o ambiente virtual na raiz do projeto, no terminal digite "python -m venv venv"
- Ative o ambiente virtual no windows: venv\scripts\activate
- no macOS: source venv/bin/activate
- Instale as dependências: pip install -r requirements.txt
- Execute as migrações do banco de dados: python manage.py migrate
- Inicie o servidor: python manage.py runserver
- Acesse o blog de receitas em seu navegador: http://localhost:8000

## English (en-us)
This is a recipe blog project developed in Django, where users can register, publish their own recipes, edit, and view recipes from other users.

# Key Features:

User Registration: Users can register on the site to create and manage their own recipes.
Recipe Publication: Users can publish their recipes, including title, ingredients, instructions, and an illustrative image.
Recipe Editing: Recipe authors can edit or delete their own recipes at any time.
Recipe Viewing: Users can view recipes from other users, including details such as ingredients, instructions, and image.
Technologies Used:

- Django
- HTML/CSS
- JavaScript
- SQLite database (by default, can be changed to other databases supported by Django)
Installation and Execution:

- Clone this repository: git clone <repository_url>
- Create virtual environment: python -m venv venv
- Activate venv on Windows: venv\scripts\activate
- Or macOS: source venv/bin/activate
- Install dependencies: pip install -r requirements.txt
- Run database migrations: python manage.py migrate
- Start the server: python manage.py runserver
- Access the recipe blog in your browser: http://localhost:8000
