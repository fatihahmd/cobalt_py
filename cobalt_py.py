import requests
class CobaltPy:
    def __init__(self, base_url):
        self.base_url = base_url
        
    def json_request(self, payload):
        url = f"{self.base_url}/api/json"
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    
    def stream_request(self, url):
        response = requests.get(url)
        return response
    
    def server_info(self):
        url = f"{self.base_url}/api/serverInfo"
        response = requests.get(url)
        return response.json()