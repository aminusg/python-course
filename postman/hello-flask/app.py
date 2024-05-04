from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_marshmallow import Marshmallow # type: ignore
import os

app = Flask(__name__)

#En este caso hemos quitado la ruta porque vamos a crear nuestro propio endpoint de la aplicación
#Vamos a guardar la base de datos en la propia app. Creamos una variable llamada basedir
#Flask necesita saber dónde guardar el SQL y vamos a llamar OS a nuestra biblioteca de sist, operativo
basedir = os.path.abspath()(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content   

class GuideSchema(ma.Schema):
    class Meta: 
        fields = ('title', 'content')

guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)

#Endpoint to create a new guide

@app.route('/guide', methods=["POST"]) #Ahora creamos un método y los valores (title y content)(necesitamos importar las librerías- request y jsonfy)
def add_guide():
    title = request.json['title']
    content = request.json['content']
#Ahora creamos una nueva variable
    new_guide = Guide(title, content)
#Ahora vamos a comunicarnos con la bbdd
    db.session.add(new_guide)
    db.session.commit() #commit es un method dentro de la biblioteca SQLAlchemy

    guide = Guide.query.get(new_guide.id) #.query es una función dentro de la biblio SQLAlchemypip

    return guide_schema.jsonify(guide)

if __name__ == '__main__':
    app.run(debug=True)
