from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import CategoriaForm
from marshmallow_shcema import CategoriaSchema
import secrets
from jwt_utils import generar_jwt

secret_key = secrets.token_hex(16)
print(secret_key)

app = Flask(__name__)


app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/flaskdb'
app.config['WTF_CSRF_ENABLED'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_actualizacion = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return self.nombre

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(300), nullable=False)
    contenido = db.Column(db.Text(), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_actualizacion = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return self.titulo

@app.route('/')
def home():
    return "Bienvenido"

@app.route('/categorias', methods=['GET'])
def obtener_categorias():
    categorias = Categoria.query.all()
    serializer = CategoriaSchema(many=True)
    return jsonify(serializer.dump(categorias))
    # return str(caregorias)
    #return jsonify([{'id': categoria.id, 'nombre': categoria.nombre} for categoria in caregorias])

@app.route('/obtener/<int:id>')
def obtener_id(id):
    print(id)
    return str(id)

@app.route('/categorias/agregar', methods=['GET', 'POST'])
def agregar_categoria():
    form = CategoriaForm()
    print(form.nombre)
    nueva_categoria = Categoria(nombre=form.nombre.data)
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoria agregada correctamente'})

@app.route('/token/<int:id>', methods=['GET'])
def obtener_token(id):
    token = generar_jwt(id, secret_key)
    return jsonify({'token': token})


if __name__ == '__main__':
    app.run(debug=True)