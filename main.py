import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'



@app.route("/asaf")
def asaf():
    return '<h1>Hello, Asaf!</h1>'


@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    result = num1 + num2
    return f'<h1>Suma: {num1} + {num2} = {result}</h1>'

@app.route("/random_fact")
def random_fact():
    facts = [
        (
            "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos."
        ),
        "Las redes sociales tienen aspectos positivos y negativos,y debemos ser conscientes de ambos cuando utilicemos estas plataformas. ",
        
    ]
    # Retorna tu diseño original más un link para volver atrás
    return f'<h1>Random Fact:</h1><p>{random.choice(facts)}</p><br><a href="/">← Ir a la pagina principal</a>'



@app.route("/<nombre>")
def saludar(nombre):
    return f'<h1>Hola, {nombre}!,eres bienvenido a esta pagina web</h1>'



app.run(debug=True)