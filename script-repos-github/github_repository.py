import json
import requests
import sys

user = sys.argv[1]
api_content = requests.get("https://api.github.com/users/{}/repos".format(user))
api_json = json.loads(api_content.text)
if not api_json:
    print("User khong co respons")
try:
    if api_json["message"] == "Not Found":
        print("User khong ton tai")
except Exception:
    for line in api_json:
        try:
            print(line['name'])
        except Exception:
            pass
