
cria o ambiente

python -m venv venv

ativar

.\venv\Scripts\activate

C:\Users\Jones\AppData\Local\Programs\Python\Python38\python.exe -m venv venv


UPDATE pip

d:\python\python_ambient\recipes_importer-19-01-2022\venv\scripts\python.exe -m pip install --upgrade pip

INSTALL BIBLIOTECAS

py -m pip install requests

CREATE Requirements

pip freeze > requirements.txt



INSTALL Requirements

python -m pip install -r requirements.txt




Executar 

py sql-comidasereceitas\main_update_recipes.py
py sql-comidasereceitas\import_recipes.py 1


# ADICIONA COM FUNCAO OTIMIZADA DE INSERÇÃO DE CUSTOM FIELDS
# GANHO DE +- 20 a 30 SEGUNDOS

py sql-comidasereceitas\import_recipes_acf.py 0 1

Argumentos 
primeiro: inicio int()
segundo: contagem int()

py sql-comidasereceitas\import_recipes.py 0 3


#############################
UPDATE CUSTOM FIELDS IN ERROR import_recipes

post_id = '20420'

py sql-comidasereceitas\update_post_custom_fields.py 56456
