1 - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
2 - python get-pip.py
3 - pip install virtualenv
4 - virtualenv venv
5 - source venv/Scripts/activate
6 - instalar o django (pip é um gerenciador de pacotes)
7 - pip install django
8 -  se quiser atualizar: pip install --upgrade pip
9 - pip freeze mostra todas as dependências
10 - pip freeze > requirements.txt cria esse arquivo com todos os requisitos
11 - django-admin help mostra todos os comandos
12 - django-admin startproject nomedoprojeto(pode ser setup . com o espaço ponto para nao criar uma pasta chamada setup e outra pasta setup dentro da setup anterior)
13 - manage.py é o arquivo responsável por rodar os comandos do django
14 - python manage.py runserver é para rodar no servidor
15 - caso voce vá em setup e depois no arquivo settings.py, tem como mudar o idioma e o fuso horário, além de voce tirar a senha secreta dará erro (pode fazer)
16 - dai basta instalar o python-dotenv e colocar a senha secreta la e apontar no settings.py
17 - crie o arquivo.env e cole la o secret e tira as aspas7
18 - importe o os no settings e também o load_dotenv para ele carregar as variáveis de ambiente(fica no env)
19 - SECRET_KEY = str(os.getenv('SECRET_KEY'))