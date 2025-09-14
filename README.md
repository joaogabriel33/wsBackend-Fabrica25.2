# wsBackend-Fabrica25.2

📘 Projeto Django – CRUD de Veículos e Marcas

Este projeto foi desenvolvido em Django e implementa um sistema de gerenciamento de Marcas e Veículos (carros e motos).
Ele contém todas as operações do CRUD (Create, Read, Update, Delete) e também consome uma API externa gratuita para buscar informações adicionais sobre veículos.

📂 Funcionalidades

Marcas

Listar marcas cadastradas

Criar nova marca

Editar marca existente

Deletar marca

Veículos

Listar veículos cadastrados

Criar novo veículo

Editar veículo existente

Deletar veículo

Integração com API externa

Busca informações sobre veículos utilizando a API Ninjas Vehicles

⚙️ Tecnologias utilizadas

Python 3.x

Django 5.x

SQLite (banco de dados padrão do Django)

HTML + Templates do Django

Requests (para consumo da API externa)

📥 Instalação e execução
1️⃣ Clonar o repositório
git clone https://github.com/joaogabriel33/wsBackend-Fabrica25.2.git
cd projetofab

2️⃣ Criar e ativar ambiente virtual
python -m venv venv


3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Configurar variáveis de ambiente

5️⃣ Rodar migrações
python manage.py migrate

6️⃣ Criar superusuário (opcional)
python manage.py createsuperuser

7️⃣ Rodar servidor
python manage.py runserver


Acesse em: http://127.0.0.1:8000/

📑 Estrutura de diretórios
projetofab/
│── appfab/               # App principal
│   ├── migrations/       
│   ├── templates/        # Templates HTML (CRUD + API externa)
│   │   ├── vehicles/
│   │   │   ├── lista-marcas.html
│   │   │   ├── criar-marcas.html
│   │   │   ├── deletar-marca.html
│   │   │   ├── lista-veic.html
│   │   │   ├── criar-veic.html
│   │   │   ├── deletar-veiculo.html
│   │   │   ├── busc-model.html
│   ├── models.py         # Modelos (Marca, Veiculo)
│   ├── views.py          # Lógica do CRUD e API
│   ├── urls.py           # Rotas do app
│
├── projetofab/           # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│
├── requirements.txt      # Dependências do projeto
├── .gitignore
├── README.md

🚗 Rotas principais
🔹 Marcas

/appfab/listamarca/ → lista marcas

/appfab/criarmarca/ → cria marca

/appfab/atualizarmarca/<int:pk>/ → edita marca

/appfab/deletarmarca/<int:pk>/ → deleta marca

🔹 Veículos

/appfab/listaveic/ → lista veículos

/appfab/criaveic/ → cria veículo

/appfab/atualizaveic/<int:pk>/ → edita veículo

/appfab/deletaveic/<int:pk>/ → deleta veículo

🔹 API externa

/appfab/buscar/ → busca informações de veículos pela API

✅ Requisitos entregues

 CRUD completo de duas entidades relacionadas (Marca e Veículo)

 Integração com API externa gratuita

 Arquivo .gitignore

 Arquivo requirements.txt

 Arquivo README.md