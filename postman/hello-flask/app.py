from flask import Flask # type: ignore

app = Flask(__name__)

#Ahora vamos a crear nuestra primera ruta y vamos a usar lo que se llama un decorador (@)
@app.route('/')
def hello():
    return "Hey Flask"

if __name__ == '__main__':
    app.run(debug=True)