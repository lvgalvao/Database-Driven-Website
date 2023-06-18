from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)

# Configurações do aplicativo
app.config.from_pyfile('config.py')

# Importando os módulos/routes
from app import models, routes
