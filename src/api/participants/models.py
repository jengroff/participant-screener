import os

from sqlalchemy.sql import func

from src import db


class Participant(db.Model):

    __tablename__ = "participants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    prospect_id = db.Column(db.String(128), nullable=True)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


# if os.getenv("FLASK_ENV") == "development":
#     from src import admin
#     from src.api.participants.admin import UsersAdminView
#
#     admin.add_view(UsersAdminView(User, db.session))
