import requests
import os
from src.looklook.auth import get_headers
from dotenv import load_dotenv
from functools import lru_cache


load_dotenv()

cookie = os.getenv("COOKIE")
hostname = os.getenv("HOSTNAME")


def get_study_invite_link(studyId: int):
    response = requests.request("GET", url, headers=get_headers())
    response = response.json()
    return invite_link


def change_prospect_status(studyId: int, prospectId: str):
    data = {"invitationState": 20}
    response = requests.request("PUT", url, json=data, headers=get_headers())
    response_json = response
    if response.status_code == 200:
        print(f"Prospect invite status has been changed from 'Queued' to 'Invited'")
    else:
        pass


@lru_cache()
def get_prospect_id_from_email(email: str) -> str:
    response = requests.request("GET", url, headers=get_headers())
    response = response.json()
    for i in response["prospects"]:
        if i["email"] == email:
            return i["id"]
        else:
            pass


def add_prospect_to_study(email: str, studyId: int):
    url = f"{hostname}/studies/{studyId}/participants"
    payload = {"emailList": [email]}
    response = requests.request("POST", url, headers=get_headers(), json=payload)
    r_json = response.json()
    prospectId = r_json["participants"][0]["id"]
    if response.status_code == 200:
        change_prospect_status(studyId, prospectId)
        print(f"{email} has been added to the study")
        invite_link = get_study_invite_link(studyId)
        return invite_link
    else:
        print("There has been an error")


def get_list_of_teams():
    url = "https://api.looklook.app/api/teams"
    response = requests.request("GET", url, headers=get_headers())
    response = response.json()
    for i in response["teams"]:
        print(f"Name: {i['name']}")
        print(f"ID: {i['id']}")
        print(f"Parent ID: {i['parentId']}\n")


def get_list_of_studies(teamId: int):
    url = f"https://api.looklook.app/api/studies?perPage=100&page=1&teamId={teamId}"
    response = requests.request("GET", url, headers=get_headers())
    json_response = response.json()
    for i in json_response["studies"]:
        print(f"Name:\t\t{i['name']}")
        print(f"id:\t\t{i['id']}")
        print(f"Participants:\t{i['meta']['participantCount']}")
        print(f"Topics:\t\t{i['meta']['topicCount']}")
        print(f"Questions:\t{i['meta']['questionCount']}")
        print(f"Groups:\t\t{i['groups']}\n")


def get_study_sentiment(
    studyId: int, keyword: str = None, score: int = -10.00, export: bool = False
):
    url = f"https://api.looklook.app/api/studies/{studyId}/analytics?layout=10&questionTypeFilter[]=10&includeModeratorReplies=false"
    response = requests.request("GET", url, headers=get_headers())
    result = response.json()

    def json_extract(obj, key):
        arr = []

        def extract(obj, arr, key):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        values = extract(obj, arr, key)
        return values

    study_text = json_extract(result, "text")
    return study_text
