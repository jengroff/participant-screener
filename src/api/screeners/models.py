import os

from sqlalchemy.sql import func

from src import db


class Screener(db.Model):

    __tablename__ = "screeners"

    screener_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    study_name = db.Column(db.String(128), nullable=False)
    study_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)

    response_1 = db.Column(db.String(255), nullable=True)
    response_2 = db.Column(db.String(255), nullable=True)
    response_3 = db.Column(db.String(255), nullable=True)
    response_4 = db.Column(db.String(255), nullable=True)
    response_5 = db.Column(db.String(255), nullable=True)

    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, study_name, name, email, phone):
        self.study_name = study_name
        self.name = name
        self.email = email
        self.phone = phone


# if os.getenv("FLASK_ENV") == "development":
#     from src import admin
#     from src.api.users.admin import UsersAdminView
#
#     admin.add_view(UsersAdminView(User, db.session))
