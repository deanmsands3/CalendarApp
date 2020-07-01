import json
class Category:

    @classmethod
    def createSuggestedCategory(self):
        standardcategories = {
            "unnecessary": 0,
            "unimportant": 1,
            "important": 2,
            "crucial": 3,
            "fixed": 4
            }
        with open('categories.json','w') as f:
            
            json.dump(standardcategories,f,indent=2)


    @classmethod
    def createOwnCategory(self, anotherCategory, categories):
        categories[anotherCategory] = len(categories)
        with open('categories.json','w',encoding='utf-8') as f:
            json.dump(categories,f,indent=2)
