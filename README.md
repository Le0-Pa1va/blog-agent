# Blog Agent – Autonomous Content Generator

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-blue)](https://www.docker.com/)
[![OpenAI](https://img.shields.io/badge/API-OpenAI-purple)](https://openai.com/)
[![Gemini](https://img.shields.io/badge/API-Gemini-orange)](https://deepmind.google/technologies/gemini)

## Description

**Blog Agent** is an autonomous content generation system designed for creating SEO-friendly blog posts using LLMs like **OpenAI GPT-4** and **Google Gemini**. It follows a modular, scalable architecture with a focus on maintainability and extensibility.

### 🛠️ Technical Overview

- **Framework**: Built on **FastAPI**, providing high-performance asynchronous APIs and OpenAPI documentation by default.
- **Modular Architecture**:
  - `app/core`: Contains the application entry point and abstract base classes for generators and models.
  - `app/api`: Defines API routes and schemas using Pydantic for data validation.
  - `app/generators`: Implements content generation logic for specific segments like `tech` and `travel`.
  - `app/models`: Encapsulates integration with LLMs (`openai_model.py`, `gemini_model.py`) through a clean interface.
  - `app/factories`: Factory classes (`generator_factory.py`, `model_factory.py`) that resolve the correct components dynamically based on input parameters.
  - `app/dependencies.py`: Handles dependency injection for MongoDB and other services.
- **Dependency Management**: All requirements are listed in `requirements.txt` and installed via Docker or virtual environments.
- **Persistence**: Posts are stored in a **MongoDB** collection for retrieval and future enhancements (e.g., versioning, analytics).
- **Environment Configuration**: The project supports `.env` configuration with support for toggling features (e.g., trends).
- **Containerized Deployment**: A `Dockerfile` and `docker-compose.yml` are included for seamless local or production-ready containerization.

This structure promotes **separation of concerns**, making it easy to add new models or content segments without modifying core logic. It's ideal for developers who want to expand content automation workflows or integrate with external platforms.

---

## 🚀 Installation

### Using Docker (Recommended)

```bash
git clone https://github.com/your-username/blog-agent.git
cd blog-agent

# Set up your API keys
cp .env.example .env
nano .env  # Add your credentials

# Launch containers
docker-compose up -d --build

# Access the docs: http://localhost:8000/docs

````
### Running Locally
```bash
python3.12 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

# Configure MongoDB in the .env file

uvicorn app.core:app --reload

```

## API Endpoints

### Generate Blog Post
**Endpoint**: `/generate`
**Method**: GET
**Parameters**:
- `model`  (optional): gpt or gemini (default: gemini)
- `segment`  (optional): Content segment (e.g., tech, travel)
- `topic` (optional): Specific topic to generate
Examples
**Exemplo**:
```http
GET /generate
```
```http
GET /generate?model=gemini&segment=tech&topic=Generative+AI
```

### List Generated Posts
**Endpoint**: `/list`
**Method**: GET


**Example**:
```http
GET /list
```

## Environment Variables
```bash
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
MONGO_URI=mongodb://localhost:27017
```