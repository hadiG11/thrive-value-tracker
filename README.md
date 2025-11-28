# thrive-value-tracker
A simple tool to track crypto project value metrics like TVL and users using APIs such as DefiLlama, inspired by Thrive Protocol's Proof of Value system to validate real impact in blockchain ecosystems.
import requests

def get_tvl(project):
    response = requests.get(f'https://api.llama.fi/tvl/{project}')
    if response.status_code == 200:
        return response.json()
    else:
        return "Error fetching TVL"
