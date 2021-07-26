import requests

from auth import get_headers
from dotenv import load_dotenv

load_dotenv()

cookie = os.getenv("COOKIE")
hostname = os.getenv("HOSTNAME")


def get_study_sentiment(studyId: int, keyword: str = None, score: int = -10.00, export: bool = False):
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
