from .app import BlogAgentAPI

api = BlogAgentAPI()
app = api.get_app()