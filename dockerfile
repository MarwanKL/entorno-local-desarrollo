# Usa una imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysqlclient


# Expone el puerto 5000 (ajusta según el puerto de tu aplicación)
EXPOSE 5000

# Comando para ejecutar tu aplicación cuando se inicie el contenedor
COPY ./start.sh /start.sh
CMD ["/bin/sh", "/start.sh"]

