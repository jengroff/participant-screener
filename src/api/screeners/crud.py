from src import db
from src.api.screeners.models import Screener


def get_all_responses():
    screener = Screener.query.all()
    return screener


def get_all_screeners():
    return Screener.query.all()


def get_response_by_study_id(study_id):
    return Screener.query.filter_by(study_id=study_id).first()


def get_response_by_screener_id(screener_id):
    return Screener.query.filter_by(id=screener_id).first()


def get_response_by_study_name(study_name):
    return Screener.query.filter_by(study_name=study_name).first()


def add_response(study_name,
                 email,
                 name,
                 phone,
                 response_1=None,
                 response_2=None,
                 response_3=None,
                 response_4=None,
                 response_5=None
                 ):
    screener = Screener(
        study_name=study_name,
        email=email,
        name=name,
        phone=phone
    )
    db.session.add(screener)
    db.session.commit()
    return screener

# def update_screener(screener_id):
#     screener.screener_id = screenername
#     screener.email = email
#     db.session.commit()
#     return screener
#
#
# def delete_screener(screener):
#     db.session.delete(screener)
#     db.session.commit()
#     return screener
