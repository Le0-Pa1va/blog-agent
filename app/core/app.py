from fastapi import FastAPI
from app.api.api import agent_router

class BlogAgentAPI:
    def __init__(self):
        self.app = FastAPI()
        self._setup_routes()

    def _setup_routes(self):
        self.app.include_router(agent_router)

    def get_app(self):
        return self.app
