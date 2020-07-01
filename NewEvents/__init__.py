import os
import json
from Category import Category as c

#The input() functions will later be replaced by the application input it is just for testing
class Event():
    def __init__(self):
        #start = self.getstarttime()
        #end = self.getendtime()
        category = self.getcategory()

    def getstarttime(self):
        start = input('Start : ')
        return start
    def getendtime(self):
        end = input('Ende : ')
        return end
    def getcategory(self):
        file = "categories.json"
        if os.stat(file).st_size==0:
            c.createSuggestedCategory()
        with open(file,"r",encoding='utf-8') as f:
            categories = json.load(f)
        cat = input('Category : ')
        if cat in categories :
            return cat
        else :
            print('choose correct category or create new one : ')
            if input('new one') == 'y':
                    c.createOwnCategory(anotherCategory=cat,categories=categories)
            else:
                print('nothing')
Event()