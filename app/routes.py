from app import app
from flask import render_template, jsonify

JOBS = [
    {
        'id': 1,
        'title': 'Dev Python',
        'description': 'Dev Python com experiência em Flask',
        'location': 'São Paulo, SP',
        'salary': 'R$ 3.000,00'
    },
    {
        'id': 2,
        'title': 'Dev Java',
        'description': 'Dev Java com experiência em Spring',
        'location': 'São Paulo, SP',
        'salary': 'R$ 4.500,00'
    },
    {
        'id': 3,
        'title': 'Dev PHP',
        'description': 'Dev PHP com experiência em Laravel',
        'location': 'São Paulo, SP'
    },
    {
        'id': 4,
        'title': 'Dev C#',
        'description': 'Dev C# com experiência em .NET',
        'location': 'Remote',
        'salary': 'R$ 3.000,00'
    }
]

@app.route('/')
def home():
    return render_template('home.html', 
                           jobs=JOBS,
                           company_name='JobsNET')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()