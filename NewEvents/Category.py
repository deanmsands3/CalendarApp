from enum import Enum, IntEnum, unique


@unique
class Category(Enum):

    @classmethod
    def createSuggestedCategory(cls):
        cls.unnecessary = 1
        cls.unimportant = 2
        cls.important = 3
        cls.crucial = 4
        cls.fixed = 5
        print(cls)

