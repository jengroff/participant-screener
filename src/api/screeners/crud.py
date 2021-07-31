from src import db
from src.api.screeners.models import Screener
from src.looklook.helper_functions import get_prospect_id_from_email


def get_all_screeners():
    return Screener.query.all()


def get_response_by_study_id(study_id):
    return Screener.query.filter_by(study_id=study_id).first()


def get_response_by_screener_id(screener_id):
    return Screener.query.filter_by(id=screener_id).first()


def get_response_by_study_name(study_name):
    return Screener.query.filter_by(study_name=study_name).first()


def add_response(
    study_name,
    prospect_email,
    prospect_name,
    prospect_phone,
    prospect_id=None,
    response_1=None,
    response_2=None,
    response_3=None,
    response_4=None,
    response_5=None,
):

    prospect_id = get_prospect_id_from_email(prospect_email)

    screener = Screener(
        study_name=study_name,
        prospect_email=prospect_email,
        prospect_name=prospect_name,
        prospect_phone=prospect_phone,
        prospect_id=prospect_id,
        response_1=response_1,
        response_2=response_2,
        response_3=response_3,
        response_4=response_4,
        response_5=response_5,
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
