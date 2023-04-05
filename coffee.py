from dataclasses import dataclass
from collections import namedtuple


@dataclass
class CoffeeDataclass:
    name: str
    strength: int
    brewing_method: str


class CoffeeSimpleClass:
    def __init__(self):
        self._name = None
        self._strength = None
        self._brewing_method = None

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength

    @property
    def brewing_method(self):
        return self._brewing_method


coffee_named_tuple = namedtuple('coffee', ('name', 'strength', 'brewing_method'))
