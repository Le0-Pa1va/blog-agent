FROM python:3.12.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app.core:app", "--host", "0.0.0.0", "--port", "8000"]
