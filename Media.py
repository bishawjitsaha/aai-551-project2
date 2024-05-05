# Description: This file is a simple class object for Media.
# It tracks ID, title, and average rating.
# It has the appropiate getters and setters for each attribute.

class Media:
    def __init__(self, id, title, avg_rating):
        self.id = id
        self.title = title
        self.avg_rating = avg_rating

    def setID(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title
    
    def setAvgRating(self, avg_rating):
        self.avg_rating = avg_rating

    def getID(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getAvgRating(self):
        return self.avg_rating
    