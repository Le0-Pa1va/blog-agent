# Blog Agent - Autônomo de Conteúdo

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen)](https://www.mongodb.com/)

## Descrição

Sistema autônomo para geração de conteúdo de blog com:

- **IA Generativa**: Integração com GPT-4 e Gemini
- **Armazenamento**: Persistência em MongoDB
- **API REST**: Interface via FastAPI

**Funcionalidades Principais**:


## Instalação

### Via Docker (Recomendado)
```bash
git clone https://github.com/seu-usuario/blog-agent.git
cd blog-agent

# Configure as chaves de API
cp .env.example .env
nano .env  # Edite com suas credenciais

# Inicie os containers
docker-compose up -d --build

# Acesse: http://localhost:8000/docs
````
### Execução Local
```bash
python3.12 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

# Configure o MongoDB local/remoto no .env

uvicorn app.main:app --reload
```

## Endpoints da API

### Geração de posts
**Endpoint**: `/generate`
**Método**: GET
**Parâmetros**:
- `model` (opcional): `gpt` ou `gemini` (padrão: `gemini`)
- `segment` (opcional): Segmento do conteúdo (pode ser: `tech`, `travel`)
- `topic` (opcional): Tópico específico para geração

**Exemplo**:
```http
GET /generate
```
```http
GET /generate?model=gemini&segment=tech&topic=IA+Generativa
```

### Listagem dos posts gerados
**Endpoint**: `/list`
**Método**: GET


**Exemplo**:
```http
GET /list
```

## Variáveis de ambiente
```bash
OPENAI_API_KEY=sua_chave_openai
GEMINI_API_KEY=sua_chave_gemini
MONGO_URI=mongodb://localhost:27017
TRENDS_ENABLED=false
```