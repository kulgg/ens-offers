import requests

def fetch(address: str, threshold: int):
    params = {
        'receiver': address,
        'status': 'active',
    }
    response = requests.get('https://ens.vision/api/offers/v1', params=params)

    if response.status_code == 200:
        data = response.json()
        offers = data["offers"]
        
        return offers
    else:
        print(response.status_code, response.reason)