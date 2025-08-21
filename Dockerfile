# Imagen base ligera de Python
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto donde correrá Streamlit
EXPOSE 8501

# Comando para lanzar Streamlit
CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]
