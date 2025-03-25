from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import os


async def get_db():
    try:
        client = AsyncIOMotorClient(
            host=os.getenv("MONGO_URI", "mongodb://mongo:27017"),
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=10000,
            socketTimeoutMS=15000,
            username=os.getenv("MONGO_USER", "root"),
            password=os.getenv("MONGO_PASS", "example"),
        )

        await client.admin.command('ping')
        print("Conexão com MongoDB estabelecida com sucesso")
        return client["blog_db"]

    except Exception as e:
        print(f"Falha na conexão com MongoDB: {e}")
        raise HTTPException(
            status_code=503,
            detail="Serviço de banco de dados indisponível"
        )
