import logging
import os
from time import sleep
import yaml
from ens_offers.fetch import fetch
from ens_offers.notify import notify_telegram
from ens_offers.persistence import Persistence

msg = "{name}.eth\n{offer}ETH by {maker} on {source}"

def get_message(name: str, offer: int, source: str, maker):
    return msg.format(name=name, offer=offer, source=source, maker=maker)

def get_decimal(price: int):
    return price / 1000000000

def load_config():
    config = {}
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def configure_logging():
    log_format = "%(asctime)s [%(levelname)s] %(module)s.%(funcName)s(): %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)

def main():
    config = load_config()
    configure_logging()
    logging.info(f"Config {config}")

    db_offers = Persistence.load_offers(config["offer_file"])
    
    try:
        while True:
            logging.info("Fetching")
            offers = fetch(config["address"], config["threshold"])

            for offer in offers:
                id = offer["_id"]
                if id in db_offers:
                    continue

                logging.info("new offer %s", id)
                db_offers.add(id)
                price = get_decimal(offer["price_decimal"])
                if price > config["threshold"] and offer["status"] == "active":
                    message = get_message(offer["name"]["name"], price, offer["source"], offer["maker"][:6])
                    notify_telegram(config["telegram"]["api-key"], config["telegram"]["chat-id"], message)
                    
            db_offers = set(list(db_offers)[-1000:])
            Persistence.save_offers(config["offer_file"], db_offers)

            sleep(config["timeout_seconds"])
    
    except Exception as e:
        notify_telegram(config["telegram"]["api-key"], config["telegram"]["chat-id"], f"[{os.path.basename(os.getcwd())}]\n{type(e).__name__}:\n{str(e)}")