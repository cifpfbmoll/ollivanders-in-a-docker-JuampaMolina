# Imagen base con Python
FROM python:3-slim-buster

# Información sobre la imagen
LABEL "edu.pingpong.ollivanders"="Ollivander's Shop" \
    version="1.0" \
    description="Ollivander's Shop Flask API" \
    maintainer="jruiz@cifpfbmoll.eu"

# Exponer en el puerto 5000
EXPOSE 5000

# Asginamos las variables de entorno para evitar que se generen archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Creamos el directorio donde copiaremos nuestro código fuente
RUN mkdir -p /usr/src/app

# Indicamos la ruta para el espacio de trabajo 
WORKDIR /usr/src/app

# Copiar los requirements dentro de el Workdir
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente en el Workdir
COPY . .

# Crear un usuario para usar la aplicación
ENV USER=appuser
RUN adduser \
    --disabled-password \
    --home "$(pwd)" \
    --no-create-home \
    "$USER"
USER appuser

# Punto de entrada de la aplicación
ENTRYPOINT ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]