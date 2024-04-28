from flask import Flask # type: ignore
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

if __name__ == '__main__':
    app.run(debug=True)
