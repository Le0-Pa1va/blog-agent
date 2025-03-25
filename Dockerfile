# Usa uma imagem base do Python
FROM python:3.10.12-slim

# Define o diretório de trabalho
WORKDIR /app

# OU
COPY requirements.txt /app/


# OU
RUN pip install -r requirements.txt

# Copia o restante do código
COPY . /app

# Expõe a porta da aplicação
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.core:app", "--host", "0.0.0.0", "--port", "8000"]