from flask_restx import Api

from src.api.ping import ping_namespace
from src.api.participants.views import participants_namespace
from src.api.screeners.views import screeners_namespace


api = Api(version="1.0", title="Study Screener API", doc="/doc")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(participants_namespace, path="/participants")
api.add_namespace(screeners_namespace, path="/screeners")
