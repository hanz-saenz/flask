from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/flaskdb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestap())
    fecha_actualizacion = db.Column(db.DateTime, default=db.func.current_timestap(), onupdate=db.func.current_timestap())

    def __repr__(self):
        return self.nombre

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(300), nullable=False)
    contenido = db.Column(db.Text(), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestap())
    fecha_actualizacion = db.Column(db.DateTime, default=db.func.current_timestap(), onupdate=db.func.current_timestap())

    def __repr__(self):
        return self.titulo

@app.route('/')
def home():
    return "Bienvenido"

@app.route('/categorias', methods=['GET'])
def obtener_categorias():
    caregorias = Categoria.query.all()

    # return str(caregorias)
    return jsonify([{'id': categoria.id, 'nombre': categoria.nombre} for categoria in caregorias])

@app.route('/obtener/<int:id>')
def obtener_id(id):
    print(id)
    return str(id)

if __name__ == '__main__':
    app.run(debug=True)