import requests 
 
class KyaruAgent :
    def __init__(self, api_token=None):
        self.key = api_token
        if not self.key:
            raise Exception("Specify API-KEY. Documentation - https://github.com/Kyaru-Development/Kyaru-api.py")

    def get(self, endpoint=None):

        if not endpoint:
            raise Exception("Specify an available endpoint. Documentation - https://github.com/Kyaru-Development/Kyaru-api.py")

        return req(endpoint, headers = 
            { 
            "Authorization": f"{self.key}" 
            } 
        )

def req(endpoint, headers):
    res = requests.get(f"https://kyaru-api.glitch.me/api/v1/{endpoint}", headers=headers)
    return res.json()

# Developer with ❤ by Kyaru Development #
