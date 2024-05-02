# Description: 

from Media import Media

class Show(Media):
    def __init__(self, id, type, title, directors, 
                actors, avg_rating, country_code, date_added, year_released, rating, duration, genres, description):
        super().__init__(id, title, avg_rating)
        self.type = type
        self.directors = directors.split('\\')
        self.actors = actors.split('\\')
        self.country_code = country_code
        self.date_added = date_added
        self.year_released = year_released
        self.rating = rating
        self.duration = duration
        self.genres = genres.split('\\')
        self.description = description

    def setType(self, type):
        self.type = type

    def setDirectors(self, directors):
        self.directors = directors

    def setActors(self, actors):
        self.actors = actors

    def setCountryCode(self, country_code):
        self.country_code = country_code

    def setDateAdded(self, date_added):
        self.date_added = date_added

    def setYearReleased(self, year_released):
        self.year_released = year_released

    def setRating(self, rating):
        self.rating = rating

    def setDuration(self, duration):
        self.duration = duration

    def setGenres(self, genres):
        self.genres = genres

    def setDescription(self, description):
        self.description = description

    def getType(self):
        return self.type

    def getDirectors(self):
        return self.directors
    
    def getActors(self):
        return self.actors
    
    def getCountryCode(self):
        return self.country_code
    
    def getDateAdded(self):
        return self.date_added
    
    def getYearReleased(self):
        return self.year_released
    
    def getRating(self):
        return self.rating
    
    def getDuration(self):
        return self.duration
    
    def getGenres(self):
        return self.genres
    
    def getDescription(self):
        return self.description
    