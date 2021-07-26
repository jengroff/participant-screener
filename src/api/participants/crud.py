from src import db
from src.api.participants.models import Participant


def get_all_participants():
    return Participant.query.all()


def get_participant_by_id(participant_id):
    return Participant.query.filter_by(id=participant_id).first()


def get_participant_by_email(email):
    return Participant.query.filter_by(email=email).first()


def add_participant(name, email, phone):
    participant = Participant(name=name, email=email, phone=phone)
    db.session.add(participant)
    db.session.commit()
    return participant


def update_participant(participant, name, email, phone):
    participant.name = name
    participant.email = email
    participant.phone = phone
    db.session.commit()
    return participant


def delete_participant(participant):
    db.session.delete(participant)
    db.session.commit()
    return participant
