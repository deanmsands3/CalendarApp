import json
class Category:
    categories=dict()
    default_categories_file="categories.json"

    @classmethod
    def createSuggestedCategory(cls):
        standardcategories = {
            "unnecessary": 0,
            "unimportant": 1,
            "important": 2,
            "crucial": 3,
            "fixed": 4
        }        
        cls.categories.update(standardcategories)
        cls.write_categories_to_file()
    
    @classmethod
    def createOwnCategory(cls, anotherCategory, categories):
        cls.categories[anotherCategory] = len(cls.categories)
        cls.write_categories_to_file()
        
    @classmethod
    def write_categories_to_file(file_name=default_categories_file)
        with open(file_name,'w') as f:
            json.dump(cls.categories,f,indent=2)
