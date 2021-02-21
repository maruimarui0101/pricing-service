from typing import Dict
import re
import requests
from bs4 import BeautifulSoup
import uuid
from common.database import Database
from models.model import Model
from dataclasses import dataclass, field


@dataclass(eq=False)
class Item(Model):
    # collection = 'items'
    collection: str = field(init=False, default="items")
    url: str
    tag_name: str
    query: Dict
    price: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    # def __init__(self, url: str, tag_name: str, query: Dict, _id=None):
    #     super().__init__()
    #     self.url = url
    #     self.tag_name = tag_name
    #     self.query = query
    #     self.price = None
    #     self._id = _id if _id is not None else uuid.uuid4().hex

    # def __post_init__(self):
    #     self.price = None

    # def __repr__(self):
    #     return f"<Item {self.url}>"

    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d\.\d\d)")
        match = pattern.search(string_price)
        found_price = match.group(0)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)

        return self.price

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "price": self.price,
            "query": self.query
        }

    # def save_to_mongo(self):
    #     Database.insert(self.collection, self.json())
    #
    # @classmethod
    # def get_by_id(cls, _id):
    #     item_json = Database.find_one('items', {'_id': _id})
    #     return cls(**item_json)

    # @classmethod
    # def all(cls):
    #     items_from_db = Database.find('items', {})
    #     return [cls(**item) for item in items_from_db]
