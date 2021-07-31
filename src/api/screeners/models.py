import os

from sqlalchemy.sql import func

from src import db


class Screener(db.Model):

    __tablename__ = "screeners"

    screener_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    study_name = db.Column(db.String(128), nullable=False)
    study_id = db.Column(db.Integer, nullable=True)
    prospect_name = db.Column(db.String(128), nullable=False)
    prospect_email = db.Column(db.String(128), nullable=False)
    prospect_phone = db.Column(db.String(128), nullable=False)
    prospect_id = db.Column(db.String(128), nullable=True)

    response_1 = db.Column(db.String(255), nullable=True)
    response_2 = db.Column(db.String(255), nullable=True)
    response_3 = db.Column(db.String(255), nullable=True)
    response_4 = db.Column(db.String(255), nullable=True)
    response_5 = db.Column(db.String(255), nullable=True)

    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(
        self,
        study_name,
        prospect_name,
        prospect_email,
        prospect_phone,
        prospect_id=None,
        response_1=None,
        response_2=None,
        response_3=None,
        response_4=None,
        response_5=None,
    ):
        self.study_name = study_name
        self.prospect_name = prospect_name
        self.prospect_email = prospect_email
        self.prospect_phone = prospect_phone
        self.prospect_id = prospect_id
        self.response_1 = response_1
        self.response_2 = response_2
        self.response_3 = response_3
        self.response_4 = response_4
        self.response_5 = response_5


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.screeners.admin import ScreenersAdminView

    admin.add_view(ScreenersAdminView(Screener, db.session))
