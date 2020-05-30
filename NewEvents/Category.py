class Category:

    @classmethod
    def createSuggestedCategory(cls):
        return {
            'unnecessary': 0,
            'unimportant': 1,
            'important': 2,
            'crucial': 3,
            'fixed': 4
        }

    @classmethod
    def createOwnCategory(cls, anotherCategory, categories):
        categories[anotherCategory] = len(categories)
        return categories
