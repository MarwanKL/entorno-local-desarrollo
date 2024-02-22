# tests/test_models.py
from app.models import Data


def test_data_model():
    # Crear una instancia de la clase Data
    data_instance = Data(id=1, name="Test Data")

    # Verificar que los atributos sean correctos
    assert data_instance.id == 1
    assert data_instance.name == "Test Data"

    # Verificar la representación de cadena (__repr__)
    assert repr(data_instance) == "<Data id=1 name=Test Data>"
