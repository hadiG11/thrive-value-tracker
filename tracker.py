import requests

def get_tvl(project):
    response = requests.get(https://api.llama.fi/tvl/{project}')
    if response.status_code == 200:
        return response.json()
    else:
        return "Error fetching TVL"
