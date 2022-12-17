import os
from typing import Set

class Persistence:
    @classmethod
    def load_offers(self, path: str) -> Set[str]:
        if not os.path.exists(path):
            return set()

        with open(path, "r") as f:
            text = f.read().splitlines()
            return set(text)

    @classmethod
    def save_offers(self, path: str, offers: Set[str]):
        with open(path, "w") as f:
            f.write("\n".join(list(offers)))