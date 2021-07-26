import requests
import os
from auth import get_headers
from dotenv import load_dotenv

load_dotenv()

cookie = os.getenv("COOKIE")
hostname = os.getenv("HOSTNAME")


def get_study_invite_link(studyId: int):
    url = f"{hostname}/studies/{studyId}"
    response = requests.request("GET", url, headers=get_headers())
    response = response.json()
    invite_link = response['study']['invitationLink']
    return invite_link


def change_prospect_status(studyId: int, prospectId: str):
    url = f"{hostname}/studies/{studyId}/participants/{prospectId}"
    data = {"invitationState": 20}
    response = requests.request("PUT", url, json=data, headers=get_headers())
    response_json = response
    if response.status_code == 200:
        print(f"Prospect invite status has been changed from 'Queued' to 'Invited'")
    else:
        pass


def get_prospectid_from_email(email: str) -> str:
    url = f"{hostname}/prospects?page=1&perPage=6000"
    response = requests.request("GET", url, headers=get_headers())
    response = response.json()
    for i in response['prospects']:
        if i['email'] == email:
            print(f"id:    {i['id']} \nemail: {email} \nname:  {i['firstName']} {i['lastName']} \nTeamID: {i['teamId']}\n")
        else:
            pass


def add_prospect_to_study(email: str, studyId: int):
    url = f"{hostname}/studies/{studyId}/participants"
    payload = {"emailList": [email]}
    response = requests.request("POST", url, headers=get_headers(), json=payload)
    r_json = response.json()
    prospectId = r_json['participants'][0]['id']
    if response.status_code == 200:
        change_prospect_status(studyId, prospectId)
        print(f"{email} has been added to the study")
        invite_link = get_study_invite_link(studyId)
        return invite_link
    else:
        print("There has been an error")


def get_list_of_teams():
    url = "https://api.looklook.app/api/teams"
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    for i in response['teams']:
        print(f"Name: {i['name']}")
        print(f"ID: {i['id']}")
        print(f"Parent ID: {i['parentId']}\n")


def get_list_of_studies(teamId: int):
    url = f"https://api.looklook.app/api/studies?perPage=100&page=1&teamId={teamId}"
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()
    for i in json_response['studies']:
        print(f"Name:\t\t{i['name']}")
        print(f"id:\t\t{i['id']}")
        print(f"Participants:\t{i['meta']['participantCount']}")
        print(f"Topics:\t\t{i['meta']['topicCount']}")
        print(f"Questions:\t{i['meta']['questionCount']}")
        print(f"Groups:\t\t{i['groups']}\n")