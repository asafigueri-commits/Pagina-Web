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

@app.route("/<nombre>")
def saludar(nombre):
    return f'<h1>Hola, {nombre}!,eres bienvenido a esta pagina web</h1>'


app.run(debug=True)