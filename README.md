# cnab-upload

## Rodando o projeto! :D

- após clonar o repositório na sua máquina, abra o projeto no seu editor de código
- dentro do terminal integrado, rode os seguintes comandos:
    - python -m venv venv
    - venv/Scripts/Activate.ps1

- Depois disso, antes de rodar o servidor, certifique de criar um arquivo .env no diretório raiz do projeto
e criar uma variável SECRET_KEY, que deve ser uma string [ exemplo no arquivo .env.example deste repositório ].

- Voltando para o terminal, basta executar estas linhas de código para rodar o servidor:
    - pip install -r requirements.txt
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver

- Feito isso, seu servidor deve estar rodando, agora é só acessar a página http://127.0.0.1:8000/ no seu navegador!