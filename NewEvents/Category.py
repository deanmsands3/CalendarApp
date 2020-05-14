from enum import IntEnum, unique, auto


@unique
class Category(IntEnum):

    def __init__(self):
        self._events = list()


Category.Unnecessary = auto()
Category.Unimportant = auto()
Category.Important = auto()
Category.HighPriority = auto()
Category.Crucial = auto()
Category.Fixed = auto()
