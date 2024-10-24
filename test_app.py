import unittest
from app import app, db, Categoria

class TestAplicacion(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            db.create_all()

    def tearDown(self):
        
        with app.app_context():
            db.session.remove()
            # db.drop_all()

    def test_obtener_categorias(self):
        respuesta = self.app.get('/categorias')
        self.assertEqual(respuesta.status_code, 200)

    def test_agregar_categoria(self):
        respuesta = self.app.post('/categorias/agregar', data={'nombre': 'Periodismo'}, follow_redirects=True)
        self.assertEqual(respuesta.status_code, 200)
        # categoria_agregada = Categoria.query.filter_by(nombre='Salud').first()
        # self.assertIsNotNone(categoria_agregada)
        # self.assertEqual(categoria_agregada.nombre, 'Salud')

if __name__ == '__main__':
    unittest.main()