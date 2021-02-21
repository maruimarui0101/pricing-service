from typing import Dict, List
from common.database import Database
import uuid
from dataclasses import dataclass, field
from models.item import Item
from models.model import Model


@dataclass(eq=False)  # no longer able to compare 2 Alert objects
class Alert(Model):
    # collection = 'alerts'
    collection: str = field(init=False, default="alerts")
    name: str
    item_id: str
    price_limit: float
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)

    # no need to call super().__init__()
    # dataclass will automatically do it, could be normal or dataclass

    # NOTE: default_factory can generate values but cannot access other object values at init


    # def __init__(self, item_id: str, price_limit: float, _id: str = None):
    #     super().__init__()
    #     self.item_id = item_id
    #     self.item = Item.get_by_id(item_id)
    #     self.price_limit = price_limit
    #     self._id = _id if _id is not None else uuid.uuid4().hex

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    # def save_to_mongo(self):
    #     Database.insert(self.collection, self.json())

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_limit_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reached a price under {self.price_limit}. Latest price is {self.item.price}")

    # @classmethod
    # def all(cls) -> list:
    #     alerts_from_db = Database.find('alerts', {})
    #     return [cls(**alert) for alert in alerts_from_db]
