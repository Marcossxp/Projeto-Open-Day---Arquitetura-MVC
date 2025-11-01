# 1º Criação dos arquivos e pastas necessárias 


Acesse o link: https://drive.google.com/drive/folders/1bAzY56Rz7xLbJnijvTsQgf-s565cZMeK?usp=sharing


arquivos
models
controllers
data
views
main.py
readme.md
requirements.txt

PS. Baixar e adicionar o arquivo csv dentro da pasta data

# 2º Adicionar ao requirements.txt as dependencias necessarias para o projeto 

Sao eles: 
 - streamlit
 - pandas
 - numpy

# 3º Criar o ambiente virtual .env

python3 -m venv .venv

# 4º Ativar o ambiente virtual

.venv/bin/activate

ou

.source .venv/bin/activate

# 5º Iniciar o vercionamento no projeto. Git 

Digite no terminal do projeto:

git init 

# 6º Instalar as dependencias do projeto --- existentes no requirements.txt 


pip install -r requirements.txt

Ps. Após essa instalação é recomendável instalar as principais atualizações para preservar as integridade e funcionalidades sempre atualizadas. Assim:

pip install --upgrade pip
pip install --upgrade streamlit pandas numpy

# 7º Criar o arquivo chamado .gitignore. Dentro dele escreva:

__paycache__/
venv/
env/
.venv/
.env/

*.log

8º Lets's Go!!

