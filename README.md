# SOFTWARE UTILIZADO

 	* Base de datos MySql
  	* Python 3.12
   	* GIT
	* Pytest



# 1-CLONAR REPOSITORIO EN LOCAL

	git clone https://github.com/MarwanKL/entorno-local-desarrollo




# 2-CREAR ENTORNO VIRTUAL

	py -m venv venv




# 3-ACTIVAR ENTORNO VIRTUAL
	
	Windows: venv\Scripts\activate
	Linux: source venv/Scripts/activate



# 4-INSTALAR DEPENDENCIAS

	pip install -r requirements.txt




# 5-INSTALAR BASE DE DATOS

	pip install flask flask-mysqldb




# 6-CREAR LAS TABLAS DE LA BASE DE DATOS
	
	py manage.py




# 7-CONFIGURAR ARCHIVO **"config.py"** PARA CONECTAR LA BASE DE DATOS

	Linea 9 establecer SQLALCHEMY_DATABASE_URI
	Ejemplo: SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "mysql://usuario:contraseña@localhost/nombre_base_datos")





# 8-COMPROBAR FUNCIONAMIENTO DE LA APLICACIÓN 

	> ENTRANDO EN "http://127.0.0.1:5000/data", SI APARECEN LOS DATOS DE LA TABLA SE HA CONSEGUIDO SATISFACTORIAMENTE LA EJECUCIÓN DE LA APLICACIÓN Y LA CONEXIÓN A LA BASE DE DATOS.




# 9-INSERTAR DATOS EN LA BASE DE DATOS PARA VERIFICAR EL FUNCIONAMIENTO DE LA APLICACIÓN 
	
	Insertar datos: curl -X POST -H "Content-Type: application/json" -d '{"name": "Nuevo Dato"}' http://127.0.0.1:5000/data


	Obtener datos: curl http://127.0.0.1:5000/data


	Eliminar los datos por id: curl -X DELETE http://127.0.0.1:5000/data/<id>




# 10-COMANDO PARA EJECUTAR PRUEBAS UNITARIAS

	pytest --cov=RUTA_REPOSITORIO_CLONADO/tests/
	IMPORTANTE instalar pytest usando "pip install pytest"

 





	



