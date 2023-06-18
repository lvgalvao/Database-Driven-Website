from flask import Flask
from flask import Flask, render_template

JOBS = [
    {
        'id': 1,
        'title': 'Desenvolvedor Python',
        'description': 'Desenvolvedor Python com experiência em Flask',
        'location': 'São Paulo, SP',
        'salary': 'R$ 3.000,00'
    },
    {
        'id': 2,
        'title': 'Desenvolvedor Java',
        'description': 'Desenvolvedor Java com experiência em Spring',
        'location': 'São Paulo, SP',
        'salary': 'R$ 4.500,00'
    },
    {
        'id': 3,
        'title': 'Desenvolvedor PHP',
        'description': 'Desenvolvedor PHP com experiência em Laravel',
        'location': 'São Paulo, SP',
        'salary': 'R$ 4.000,00'
    },
    {
        'id': 4,
        'title': 'Desenvolvedor C#',
        'description': 'Desenvolvedor C# com experiência em .NET',
        'location': 'Remote',
        'salary': 'R$ 3.000,00'
    }
]

app = Flask(__name__)

# Configurações do aplicativo
app.config.from_pyfile('config.py')

# Importando os módulos/routes
from app import models, routes
