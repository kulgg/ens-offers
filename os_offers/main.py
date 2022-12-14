import yaml
from os_offers.fetch import fetch
from os_offers.notify import notify_telegram


msg = "{name}\n{offer} by {maker} on {source}"

def get_message(name: str, offer: int, source: str, maker):
    return msg.format(name=name, offer=offer, source=source, maker=maker)

def get_decimal(price: int):
    return price / 1000000000

def load_config():
    config = {}
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def main():
    config = load_config()
    print("Config", config)
    
    try:
        offers = fetch(config["address"], config["threshold"])

        for offer in offers:
            price = get_decimal(offer["price_decimal"])
            if price > config["threshold"] and offer["status"] == "active":
                message = get_message(offer["name"]["name"], price, offer["source"], offer["maker"][:6])
                notify_telegram(config["telegram"]["api-key"], config["telegram"]["chat-id"], message)
                print("Offer id", offer["_id"])
                print("")
    except Exception as e:
        notify_telegram(config["telegram"]["api-key"], config["telegram"]["chat-id"], e)