Delegacia Project

Sistema simples de gerenciamento de ocorrências policiais desenvolvido com Django.
Permite cadastrar ocorrências, suspeitos, vítimas, policiais, anexar evidências (fotos) e gerenciar registros de forma prática.

Observação: este README é um template — ajuste instruções específicas (variáveis de ambiente, serviços externos) conforme seu ambiente.

Sumário

Funcionalidades

Tecnologias

Requisitos

Instalação rápida

Configuração

Executando localmente

Estrutura do projeto

Templates principais

Deploy / Produção

Testes

Contribuição

Licença

Contato

Funcionalidades

Cadastro e listagem de ocorrências.

Cadastro de suspeitos, vítimas e policiais.

Upload de evidências (imagens) associadas às ocorrências.

Autenticação (login/logout).

Páginas administrativas básicas via Django Admin.

Templates com base.html e herança para as páginas internas.

Tecnologias

Python 3.10+

Django 5.x (o projeto foi testado com Django 5.2.7)

SQLite (por padrão, pode trocar para PostgreSQL/MySQL em produção)

Frontend simples com templates Django (HTML/CSS)

Requisitos

Git

Python 3.10+

pip (ou Poetry/Poetry/venv conforme sua preferência)

Instalação rápida (local)
# clonar repositório
git clone <URL-DO-REPO>
cd delegacia_project

# criar e ativar virtualenv (exemplo com venv)
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

# instalar dependências
pip install -r requirements.txt


Se não houver requirements.txt, gere com:
pip freeze > requirements.txt após instalar django e outras libs que usar.

Configuração

Crie um arquivo .env (ou configure settings.py conforme preferir). Exemplo mínimo:

DEBUG=True
SECRET_KEY=cole_sua_secret_key_aqui
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
MEDIA_ROOT=media/
MEDIA_URL=/media/


No settings.py verifique:

Configuração de MEDIA_ROOT/MEDIA_URL para upload de evidências.

Configuração de STATIC_ROOT/STATIC_URL para arquivos estáticos.

Migrações e superuser
# criar migrations e aplicar
python manage.py makemigrations
python manage.py migrate

# criar superuser (para acessar /admin/)
python manage.py createsuperuser

Executando localmente
# coletar estáticos (se precisar)
python manage.py collectstatic --noinput

# rodar servidor de desenvolvimento
python manage.py runserver
# acessar em http://127.0.0.1:8000/


Se estiver usando uploads de imagens em desenvolvimento, assegure-se de servir arquivos de mídia pelo Django (em urls.py principal):

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... suas rotas ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Estrutura do projeto (resumida)
delegacia_project/
├─ core/                      # app principal
│  ├─ templates/core/
│  │  ├─ base.html
│  │  ├─ home.html
│  │  ├─ login.html
│  │  ├─ form.html
│  │  ├─ ocorrencia_list.html
│  │  ├─ suspeito_list.html
│  │  ├─ vitima_list.html
│  │  ├─ policial_list.html
│  │  ├─ evidencia_list.html
│  │  └─ confirm_delete.html
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  ├─ urls.py
│  └─ admin.py
├─ delegacia_project/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py / asgi.py
└─ manage.py

Templates principais

base.html — layout base com blocos reutilizáveis ({% block content %} etc.).

home.html — dashboard/página inicial.

login.html — formulário de login.

form.html — template genérico para criação/edição de registros.

Listagens: ocorrencia_list.html, suspeito_list.html, vitima_list.html, policial_list.html, evidencia_list.html.

confirm_delete.html — confirmação de exclusão.

As views devem estender base.html e usar blocos para conteúdo principal.

Upload de evidências (imagens)

Utilize um campo ImageField em seu model de evidência, por exemplo:

from django.db import models

class Evidencia(models.Model):
    ocorrencia = models.ForeignKey('Ocorrencia', on_delete=models.CASCADE, related_name='evidencias')
    imagem = models.ImageField(upload_to='evidencias/%Y/%m/%d/')
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)


Contato

Autor: Icaro Mota

Email: Icaro2ico@hotmail.com
