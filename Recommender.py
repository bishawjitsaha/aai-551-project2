# Description: 

from collections import Counter
from tkinter import filedialog
from Book import Book
from Show import Show

class Recommender:
    def __init__(self):
        self.book_dict = {}
        self.show_dict = {}
        self.associations = {}

    def loadBooks(self):
        while True:
            file_path = filedialog.askopenfilename()
            if file_path.endswith('.csv'):
                break
            else:
                print('Invalid file type. Please select a .csv file.')

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().split(',')
                currBook = Book(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10])
                self.book_dict[line[0]] = currBook
            
    def loadShows(self):
        while True:
            file_path = filedialog.askopenfilename()
            if file_path.endswith('.csv'):
                break
            else:
                print('Invalid file type. Please select a .csv file.')

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().split(',')
                currShow = Show(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12])
                self.show_dict[line[0]] = currShow

    def loadAssociations(self):
        while True:
            file_path = filedialog.askopenfilename()
            if file_path.endswith('.csv'):
                break
            else:
                print('Invalid file type. Please select a .csv file.')

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().split(',')

                if line[0] not in self.associations:
                    self.associations[line[0]] = {line[1]: 1}
                else:
                    if line[1] not in self.associations[line[0]]:
                        self.associations[line[0]][line[1]] = 1
                    else:
                        self.associations[line[0]][line[1]] += 1

                if line[1] not in self.associations:
                    self.associations[line[1]] = {line[0]: 1}
                else:
                    if line[1] not in self.associations[line[1]]:
                        self.associations[line[1]][line[0]] = 1
                    else:
                        self.associations[line[1]][line[0]] += 1
                

    def getMovieList(self):
        movieList = [{'title': movie.getTitle(), 'runtime': movie.getDuration()} for movie in self.show_dict.values() if movie.getType() == 'Movie']
        longest_title_length = max(len(movie['title']) for movie in movieList)
        # print(longest_title_length, movieList)
        return longest_title_length, movieList

    def getTVList(self):
        tvShowList = [{'title': tvShow.getTitle(), 'seasons': tvShow.getDuration()} for tvShow in self.show_dict.values() if tvShow.getType() == 'TV Show']
        longest_title_length = max(len(tvShow['title']) for tvShow in tvShowList)
        # print(longest_title_length, movieList)
        return longest_title_length, tvShowList

    def getBookList(self):
        bookList = [{'title': book.getTitle(), 'authors': ', '.join(book.getAuthors())} for book in self.book_dict.values() if book.getTitle() != 'title']
        longest_title_length = max(len(book['title']) for book in bookList)
        # print(longest_title_length, bookList)
        return longest_title_length, bookList
    
    def getMovieRatings(self):
        movieList = [movie for movie in self.show_dict.values() if movie.getType() == 'Movie']
        totalRatingList = []
        
        for movie in movieList:
            if movie.getRating() not in ['rating']:
                if movie.getRating() == '':
                    movie.setRating('None')
                totalRatingList.append(movie.getRating())
                
        return self.count_ratings(totalRatingList)
    
    def getTVRatings(self):
        tvShowList = [movie for movie in self.show_dict.values() if movie.getType() == 'TV Show']
        totalRatingList = []

        for tvShow in tvShowList:
            if tvShow.getRating() not in ['rating']:
                if tvShow.getRating() == '':
                    tvShow.setRating('None')
                totalRatingList.append(tvShow.getRating())
        
        return self.count_ratings(totalRatingList)

    def count_ratings(self, ratings_list):
        ratings_count = {}
        for rating in ratings_list:
            if rating in ratings_count:
                ratings_count[rating] += 1
            else:
                ratings_count[rating] = 1
        return ratings_count

    def getMovieStats(self):
        movieList = [movie for movie in self.show_dict.values() if movie.getType() == 'Movie']
        totalRatingList = []
        totalDurationList = []
        directorList = []
        actorList = []
        genreList = []

        for movie in movieList:
            if movie.getRating() not in ['rating']:
                if movie.getRating() == '':
                    movie.setRating('None')
                totalRatingList.append(movie.getRating())

            if movie.getDuration() not in ['duration', ""]:
                totalDurationList.append(movie.getDuration())
            
            currDirectors = [director for director in movie.getDirectors() if director not in ['directors', ""]]
            directorList.extend(currDirectors)

            currActors = [actor for actor in movie.getActors() if actor not in ['actors', ""]]
            actorList.extend(currActors)

            currGenres = [genre for genre in movie.getGenres() if genre not in ['genres', ""]]
            genreList.extend(currGenres)


       
        # ratings breakdown in percentages
        ratingCounter = Counter(totalRatingList)
        totalRatings = len(totalRatingList)
        ratingPercentages = [rating + " " + "{:.2f}".format((count / totalRatings) * 100) + '%' for rating, count in ratingCounter.items()]
        # print(ratingPercentages)

        # average movie duration in minutes with two decimals of precision
        totalDurationList = [int(duration.split(" ")[0]) for duration in totalDurationList]
        avgDuration = "{:.2f}".format(sum(totalDurationList) / len(totalDurationList)) + " minutes"

        # most common director
        directorCounter = Counter(directorList)
        # max_director_count = max(directorCounter.values())
        # most_common_directors = [director for director, count in directorCounter.items() if count == max_director_count]
        # most_common_directors = ', '.join(most_common_directors)
        most_common_directors = directorCounter.most_common(1)[0][0]

        # most common actor
        actorCounter = Counter(actorList)
        # max_actor_count = max(actorCounter.values())
        # most_common_actors = [actor for actor, count in actorCounter.items() if count == max_actor_count]
        # most_common_actors = ', '.join(most_common_actors)
        most_common_actors = actorCounter.most_common(1)[0][0]

        # most common genre
        genreCounter = Counter(genreList)
        # max_genre_count = max(genreCounter.values())
        # most_common_genres = [genre for genre, count in genreCounter.items() if count == max_genre_count]
        # most_common_genres = ', '.join(most_common_genres)
        most_common_genres = genreCounter.most_common(1)[0][0]

        return ratingPercentages, avgDuration, most_common_directors, most_common_actors, most_common_genres

    def getTVStats(self):
        tvShowList = [movie for movie in self.show_dict.values() if movie.getType() == 'TV Show']
        totalRatingList = []
        totalDurationList = []
        actorList = []
        genreList = []

        for tvShow in tvShowList:
            if tvShow.getRating() not in ['rating']:
                if tvShow.getRating() == '':
                    tvShow.setRating('None')
                totalRatingList.append(tvShow.getRating())

            if tvShow.getDuration() not in ['duration', ""]:
                totalDurationList.append(tvShow.getDuration())

            currActors = [actor for actor in tvShow.getActors() if actor not in ['actors', ""]]
            actorList.extend(currActors)

            currGenres = [genre for genre in tvShow.getGenres() if genre not in ['genres', ""]]
            genreList.extend(currGenres)


       
        # ratings breakdown in percentages
        ratingCounter = Counter(totalRatingList)
        totalRatings = len(totalRatingList)
        ratingPercentages = [rating + " " + "{:.2f}".format((count / totalRatings) * 100) + '%' for rating, count in ratingCounter.items()]
        # print(ratingPercentages)

        # average movie duration in minutes with two decimals of precision
        totalDurationList = [int(duration.split(" ")[0]) for duration in totalDurationList]
        avgDuration = "{:.2f}".format(sum(totalDurationList) / len(totalDurationList)) + " seasons"

        # most common actor
        actorCounter = Counter(actorList)
        # max_actor_count = max(actorCounter.values())
        # most_common_actors = [actor for actor, count in actorCounter.items() if count == max_actor_count]
        # most_common_actors = ', '.join(most_common_actors)
        most_common_actors = actorCounter.most_common(1)[0][0]

        # most common genre
        genreCounter = Counter(genreList)
        # max_genre_count = max(genreCounter.values())
        # most_common_genres = [genre for genre, count in genreCounter.items() if count == max_genre_count]
        # most_common_genres = ', '.join(most_common_genres)
        most_common_genres = genreCounter.most_common(1)[0][0]

        return ratingPercentages, avgDuration, most_common_actors, most_common_genres

    def getBookStats(self):
        pageList = []
        authorList = []
        publisherList = []

        for book in self.book_dict.values():
            if book.getPages() not in ['num_pages', ""]:
                pageList.append(int(book.getPages()))

            currAuthors = book.getAuthors()
            authorList.extend(currAuthors)

            if book.getPublisher() not in ['publisher', ""]:
                publisherList.append(book.getPublisher())
        
        # average book length in pages
        avgPages = "{:.2f}".format(sum(pageList) / len(pageList)) + " pages"

        # most common author
        authorCounter = Counter(authorList)
        most_common_authors = authorCounter.most_common(1)[0][0]

        # most common publisher
        publisherCounter = Counter(publisherList)
        most_common_publishers = publisherCounter.most_common(1)[0][0]

        return avgPages, most_common_authors, most_common_publishers

    def searchTVMovies(self, type, title, director, actor, genre):
        if type not in ['Movie', 'TV Show']:
            raise Exception('Invalid type. Please enter either "Movie" or "TV Show".')
        
        if title == '' and director == '' and actor == '' and genre == '':
            raise Exception('Please enter a value for each field.')
        
        params = {}

        if title != '': params['title'] = title
        if director != '': params['director'] = director
        if actor != '': params['actor'] = actor
        if genre != '': params['genre'] = genre

        ret = []

        if type == 'Movie':
            movieList = [movie for movie in self.show_dict.values() if movie.getType() == 'Movie']
            for key, value in params.items():
                for movie in movieList:
                    movieTemp = {"title": movie.getTitle(), "director": movie.getDirectors(), "actor": movie.getActors(), "genre": movie.getGenres()} 
                    if value in movieTemp[key]:
                        ret.append(movieTemp)

        else:
            tvShowList = [tvShow for tvShow in self.show_dict.values() if tvShow.getType() == 'TV Show']
            for key, value in params.items():
                for tvShow in tvShowList: 
                    showTemp = {"title": tvShow.getTitle(), "director": tvShow.getDirectors(), "actor": tvShow.getActors(), "genre": tvShow.getGenres()}
                    if value in showTemp[key]:
                        ret.append(showTemp)
        return ret

    def searchBooks(self, title, author, publisher):
        if title == '' and author == '' and publisher == '':
            raise Exception('Please enter a value for each field.')
        
        params = {}

        if title != '': params['title'] = title
        if author != '': params['author'] = author
        if publisher != '': params['publisher'] = publisher

        ret = []

        bookList = [book for book in self.book_dict.values()]
        for key, value in params.items():
            for book in bookList: 
                bookTemp = {"title": book.getTitle(), "author": book.getAuthors(), "publisher": book.getPublisher()}
                if value in bookTemp[key]:
                    ret.append(bookTemp)

        return ret

    def getRecommendations(self, type, title):
        if type not in ['Movie', 'TV Show', "Book"]:
            raise Exception('Invalid type. Please enter either "Movie", "TV Show", or "Book".')
        
        if title == '':
            raise Exception('Please enter a value for each field.')
        
        ret = []
        
        if type == 'Movie':
            movieList = [movie for movie in self.show_dict.values() if movie.getType() == 'Movie' and movie.getTitle() == title]
            if len(movieList) == 0:
                raise Exception('No movie found with that title.')
            
            for movie in movieList:
                # print("items: ")
                # print(self.associations[movie.getID()].items())
                sorted_associations = dict(sorted(self.associations[movie.getID()].items(), key=lambda item: item[1]))
                for key, value in sorted_associations.items():
                    currBook = self.book_dict[key]
                    ret.append({"Title": currBook.getTitle(), 
                                "Author": currBook.getAuthors(),
                                "Average Rating": currBook.getAvgRating(),
                                "ISBN": currBook.getISBN(),
                                "ISBN13": currBook.getISBN13(),
                                "Language Code": currBook.getLang(),
                                "Pages": currBook.getPages(),
                                "Rating Count": currBook.getRatingCount(),
                                "Publication Date": currBook.getPublication(),
                                "Publisher": currBook.getPublisher()})

        elif type == 'TV Show':
            tvShowList = [tvShow for tvShow in self.show_dict.values() if tvShow.getType() == 'TV Show' and tvShow.getTitle() == title]
            if len(tvShowList) == 0:
                raise Exception('No TV Show found with that title.')
            
            for tvShow in tvShowList:
                sorted_associations = dict(sorted(self.associations[tvShow.getID()].items(), key=lambda item: item[1]))
                for key, value in sorted_associations.items():
                    currBook = self.book_dict[key]
                    ret.append({"Title": currBook.getTitle(), 
                                "Author": currBook.getAuthors(),
                                "Average Rating": currBook.getAvgRating(),
                                "ISBN": currBook.getISBN(),
                                "ISBN13": currBook.getISBN13(),
                                "Language Code": currBook.getLang(),
                                "Pages": currBook.getPages(),
                                "Rating Count": currBook.getRatingCount(),
                                "Publication Date": currBook.getPublication(),
                                "Publisher": currBook.getPublisher()})

        else:
            bookList = [book for book in self.book_dict.values() if book.getTitle() == title]
            if len(bookList) == 0:
                raise Exception('No book found with that title.')
            
            for book in bookList:
                sorted_associations = dict(sorted(self.associations[book.getID()].items(), key=lambda item: item[1]))
                for key, value in sorted_associations.items():
                    currShow = self.show_dict[key]
                    ret.append({"Title": currShow.getTitle(),
                                "Type": currShow.getType(),
                                "Directors": currShow.getDirectors(),
                                "Actors": currShow.getActors(),
                                "Average Rating": currShow.getAvgRating(),
                                "Country Code": currShow.getCountryCode(),
                                "Date Added": currShow.getDateAdded(),
                                "Year Released": currShow.getYearReleased(),
                                "Rating": currShow.getRating(),
                                "Duration": currShow.getDuration(),
                                "Genres": currShow.getGenres(),
                                "Description": currShow.getDescription()})
        
        return ret
                      
                