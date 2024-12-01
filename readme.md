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
19 - SECRET_KEY = str(os.getenv('SECRET_KEY')) ainda no settings
20 - se eu colocar mais funcionalidade são chamados de app, dai basta usar o comando python manage.py startapp galeria (vai criar uma pasta com tudo dentro)
21 - agora preciso dizer a galeria que ele vai fazer parte do projeto, então vou la em settings e coloco na lista INSTALLED_APPS o nome do app 'galeria'
22 - indo la no galeria temos o views.py la que dizemos que vai ser visualizado o dado
23 - o comando collectstatic diga ao django onde está os arquivos static (css, js), então o comando pip install collectstatic gera a pasta static e basta colocar la dentro o css e demais arquivos
24 - para carregar tu deve usar <% load static  %> antes do doctype
25 - além disso, necessário carregar arquivos e imagens utilizando {%static ''%}
26 - quando é link {% url'imagem'%} nao pode esquecer de criar a funcao e a rota

OBS: o comando caso voce pegue do git é python -m virtualenv .env, para
Sempre para instalar tudo faça
1 - entra no ambiente virtual
2 - pip install -r requirements.txt
3 - Dê o makemigrations e depois o migrate
4 - Você pode chamar o galeria.apps.GaleriaConfig no INSTALLED_APPS no settings para além de chamar so o aplicativo, ele chama toda a configuração.