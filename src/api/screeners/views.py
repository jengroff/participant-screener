from flask import request
from flask_restx import Namespace, Resource, fields

from src.api.screeners.crud import (
        get_all_responses,
        get_response_by_screener_id,
        add_response
)

screeners_namespace = Namespace("screeners")


screener = screeners_namespace.model(
    "Screener",
    {
        "screener_id": fields.Integer(readOnly=True),
        "prospect_name": fields.String(required=True),
        "prospect_email": fields.String(required=True),
        "prospect_phone": fields.String(required=True),
        "prospect_id": fields.String(required=False),
        "study_name": fields.String(required=True),
        "response_1": fields.String(required=False),
        "response_2": fields.String(required=False),
        "response_3": fields.String(required=False),
        "response_4": fields.String(required=False),
        "response_5": fields.String(required=False),
        "created_date": fields.DateTime(),
    },
)


class ScreenerList(Resource):
    @screeners_namespace.marshal_with(screener, as_list=True)
    def get(self):
        """Returns all screener responses."""
        return get_all_responses(), 200

    @screeners_namespace.expect(screener, validate=True)
    @screeners_namespace.response(201, "<screener_response> was added!")
    @screeners_namespace.response(400, "Sorry. That response was already submitted.")
    def post(self):
        """Creates a new screener."""
        post_data = request.get_json()
        study_name = post_data.get("study_name")
        prospect_email = post_data.get("prospect_email")
        prospect_name = post_data.get("prospect_name")
        prospect_phone = post_data.get("prospect_phone")
        prospect_id = post_data.get("prospect_id")
        response_1 = post_data.get("response_1")
        response_2 = post_data.get("response_2")
        response_3 = post_data.get("response_3")
        response_4 = post_data.get("response_4")
        response_5 = post_data.get("response_5")

        response_object = {}

        add_response(study_name,
                     prospect_email,
                     prospect_name,
                     prospect_phone,
                     prospect_id,
                     response_1,
                     response_2,
                     response_3,
                     response_4,
                     response_5)

        response_object = response_object.update(add_response())
        return response_object, 201


class Screeners(Resource):
    @screeners_namespace.marshal_with(screener)
    @screeners_namespace.response(200, "Success")
    @screeners_namespace.response(404, "Screener <screener_id> does not exist")
    def get(self, screener_id):
        """Returns a single screener."""
        screener = get_response_by_screener_id(screener_id)
        if not screener:
            screeners_namespace.abort(404, f"Screener {screener_id} does not exist")
        return screener, 200

    # @screeners_namespace.expect(screener, validate=True)
    # @screeners_namespace.response(200, "<screener_id> was updated!")
    # @screeners_namespace.response(400, "Sorry. That email already exists.")
    # @screeners_namespace.response(404, "User <screener_id> does not exist")
    # def put(self, screener_id):
    #     """Updates a screener."""
    #     post_data = request.get_json()
    #     screenername = post_data.get("screenername")
    #     email = post_data.get("email")
    #     response_object = {}
    #
    #     screener = get_screener_by_id(screener_id)
    #     if not screener:
    #         screeners_namespace.abort(404, f"User {screener_id} does not exist")
    #
    #     if get_screener_by_email(email):
    #         response_object["message"] = "Sorry. That email already exists."
    #         return response_object, 400
    #
    #     update_screener(screener, screenername, email)
    #
    #     response_object["message"] = f"{screener.id} was updated!"
    #     return response_object, 200
    #
    # @screeners_namespace.response(200, "<screener_id> was removed!")
    # @screeners_namespace.response(404, "User <screener_id> does not exist")
    # def delete(self, screener_id):
    #     """ "Deletes a screener."""
    #     response_object = {}
    #     screener = get_screener_by_id(screener_id)
    #
    #     if not screener:
    #         screeners_namespace.abort(404, f"User {screener_id} does not exist")
    #
    #     delete_screener(screener)
    #
    #     response_object["message"] = f"{screener.email} was removed!"
    #     return response_object, 200


screeners_namespace.add_resource(ScreenerList, "")
screeners_namespace.add_resource(Screeners, "/<int:screener_id>")
