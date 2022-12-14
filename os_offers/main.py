import requests
import yaml

eth_decimals = 1000000000

def fetch(address: str, threshold: int):
    params = {
        'receiver': address,
        'status': 'active',
    }
    response = requests.get('https://ens.vision/api/offers/v1', params=params)

    if response.status_code == 200:
        data = response.json()
        offers = data["offers"]
        
        for offer in offers:
            price = offer["price_decimal"] / eth_decimals
            if price > threshold:
                print("Offer id", offer["_id"])
                print("Name", offer["name"]["name"])
                print("Price", price)
                print("Source", offer["source"])
                print("Status", offer["status"])
                print("")
    else:
        print(response.status_code, response.reason)

def load_config():
    config = {}
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def main():
    config = load_config()
    print("Config", config)
    
    fetch(config["address"], config["threshold"])