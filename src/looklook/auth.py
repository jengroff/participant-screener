from typing import Dict, Any, Union, Optional

import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
cookie = os.getenv("COOKIE")
url = os.getenv("URL")


def get_bearer_token():
    url = "https://api.looklook.app/api/auth/login"
    payload = json.dumps({"email": email, "password": password})
    headers = {"Content-Type": "application/json", "Cookie": cookie}
    response = requests.request("POST", url, headers=headers, data=payload)
    response = response.json()
    token = response["token"]
    return token


def get_headers():
    headers: dict[str, Union[Optional[str], Any]] = {
        "Authorization": get_bearer_token(),
        "Cookie": cookie,
    }
    return headers
