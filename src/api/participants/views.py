from flask import request
from flask_restx import Namespace, Resource, fields

from src.api.participants.crud import (
    get_all_participants,
    get_participant_by_email,
    add_participant,
    get_participant_by_id,
    update_participant,
    delete_participant,
)

participants_namespace = Namespace("participants")


participant = participants_namespace.model(
    "Participant",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True),
        "email": fields.String(required=True),
        "phone": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)


class ParticipantsList(Resource):
    @participants_namespace.marshal_with(participant, as_list=True)
    def get(self):
        """Returns all participants."""
        return get_all_participants(), 200

    @participants_namespace.expect(participant, validate=True)
    @participants_namespace.response(201, "<participant_email> was added!")
    @participants_namespace.response(400, "Sorry. That email already exists.")
    def post(self):
        """Creates a new participant."""
        post_data = request.get_json()
        name = post_data.get("name")
        email = post_data.get("email")
        phone = post_data.get("phone")

        response_object = {}

        participant = get_participant_by_email(email)
        if participant:
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400

        add_participant(name, email, phone)

        response_object["message"] = f"{email} was added!"
        return response_object, 201


class Participants(Resource):
    @participants_namespace.marshal_with(participant)
    @participants_namespace.response(200, "Success")
    @participants_namespace.response(404, "Participant <participant_id> does not exist")
    def get(self, participant_id):
        """Returns a single participant."""
        participant = get_participant_by_id(participant_id)
        if not participant:
            participants_namespace.abort(404, f"Participant {participant_id} does not exist")
        return participant, 200

    @participants_namespace.expect(participant, validate=True)
    @participants_namespace.response(200, "<participant_id> was updated!")
    @participants_namespace.response(400, "Sorry. That email already exists.")
    @participants_namespace.response(404, "Participant <participant_id> does not exist")
    def put(self, participant_id):
        """Updates a participant."""
        post_data = request.get_json()
        name = post_data.get("name")
        email = post_data.get("email")
        phone = post_data.get("phone")
        response_object = {}

        participant = get_participant_by_id(participant_id)
        if not participant:
            participants_namespace.abort(404, f"Participant {participant_id} does not exist")

        if get_participant_by_email(email):
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400

        update_participant(participant, name, email, phone)

        response_object["message"] = f"{participant.id} was updated!"
        return response_object, 200

    @participants_namespace.response(200, "<participant_id> was removed!")
    @participants_namespace.response(404, "Participant <participant_id> does not exist")
    def delete(self, participant_id):
        """ "Deletes a participant."""
        response_object = {}
        participant = get_participant_by_id(participant_id)

        if not participant:
            participants_namespace.abort(404, f"Participant {participant_id} does not exist")

        delete_participant(participant)

        response_object["message"] = f"{participant.email} was removed!"
        return response_object, 200


participants_namespace.add_resource(ParticipantsList, "")
participants_namespace.add_resource(Participants, "/<int:participant_id>")
