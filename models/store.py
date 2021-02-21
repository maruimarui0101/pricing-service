from models.model import Model
import uuid
from typing import Dict
from common.database import Database
import re
from dataclasses import dataclass, field


@dataclass(eq=False)
class Store(Model):
    # collection = "stores"
    collection: str = field(init=False, default="stores")
    name: str
    url_prefix: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    # def __init__(self, name: str, url_prefix: str, tag_name: str, query: Dict, _id: str = None):
    #     super().__init__()
    #     self.name = name
    #     self.url_prefix = url_prefix
    #     self.tag_name = tag_name
    #     self.query = query
    #     self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_name(cls, store_name: str) -> "Store":
        return cls.find_one_by('name', store_name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> "Store":
        url_regex = {"$regex": "^{}".format(url_prefix)}
        return cls.find_one_by('url_prefix', url_regex)

    @classmethod
    def find_by_url(cls, url: str) -> "Store":
        """
        Return a store from a url"
        :param url: The item's URL
        :return: a Store
        """
        pattern = re.compile(r"(https?://.*?/)")
        match = pattern.search(url)
        url_prefix = match.group(1)
        print(url_prefix)
        return cls.get_by_url_prefix(url_prefix)
