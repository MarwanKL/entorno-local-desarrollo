# tests/test_routes.py
from flask import Flask
from app import db
from app.models import Data
from app.routes import data_routes

def test_insert_data_route():
    # Crear una aplicación Flask para las pruebas
    test_app = Flask(__name__)
    test_app.config['TESTING'] = True
    test_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Configurar la aplicación de prueba con la extensión SQLAlchemy
    db.init_app(test_app)

    # Crear las tablas en la base de datos de prueba
    with test_app.app_context():
        db.create_all()

    # Configurar la aplicación de prueba con las rutas
    test_app.register_blueprint(data_routes)

    # Simular una solicitud POST a la ruta de inserción de datos
    with test_app.test_client() as client:
        response = client.post("/data", json={"name": "Test Data"})

    # Verificar la respuesta
    assert response.status_code == 200
    assert response.json == {"message": "Data inserted successfully"}

    # Verificar que los datos se han insertado en la base de datos de prueba
    with test_app.app_context():
        data_count = Data.query.filter_by(name="Test Data").count()
        assert data_count == 1

def test_get_all_data_route():
    # Similar a test_insert_data_route, pero para la ruta de obtener todos los datos
    # Puedes crear más pruebas para otras rutas según sea necesario
    pass

def test_delete_data_route():
    # Similar a test_insert_data_route, pero para la ruta de eliminar datos por ID
    # Puedes crear más pruebas para otras rutas según sea necesario
    pass
