# Description: This file is a GUI for the Media Recommender project.
# It allows the user to load shows, books, and recommendations.
# It also allows the user to search for shows, books, and get recommendations.
# EXTRA CREDIT: It also allows the user to generate charts for the ratings of movies and TV shows.

import os
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import Recommender
import tkinter as tk
from tkinter import ttk

class RecommenderGUI:
    def __init__(self):
        """ 
        Initializes the GUI and the Recommender object.
        """
        self.recc = Recommender.Recommender()

        self.main_window = tk.Tk()
        self.main_window.title("Media Recommender")
        self.main_window.geometry("1200x800")
        self.notebook = ttk.Notebook(self.main_window)

        #region MOVIE TAB
        self.movieTab = ttk.Frame(self.main_window)
        self.notebook.add(self.movieTab, text="Movies")

        self.movieTopFrame = ttk.Frame(self.movieTab)
        self.movieTopFrame.grid(row=0, column=0, sticky="new")
        self.movieTab.grid_rowconfigure(0, weight=1)

        self.movieBottomFrame = ttk.Frame(self.movieTab)
        self.movieBottomFrame.grid(row=1, column=0, sticky="sew")
        self.movieTab.grid_rowconfigure(1, weight=1)
        self.movieTab.grid_columnconfigure(0, weight=1) 

        movieScrollbar = tk.Scrollbar(self.movieTopFrame)
        movieScrollbar.grid(row=0, column=1, sticky='ns')

        self.topMoiveText = tk.Text(self.movieTopFrame, yscrollcommand=movieScrollbar.set)
        self.topMoiveText.grid(row=0, column=0, sticky='nsew')
        self.movieTopFrame.grid_columnconfigure(0, weight=1)
        self.movieTopFrame.grid_rowconfigure(0, weight=1)

        movieScrollbar.config(command=self.topMoiveText.yview)

        self.topMoiveText.insert(1.0, "No Movies Loaded\n")
        self.topMoiveText.config(state=tk.DISABLED)

        self.bottomMovieStatText = tk.Text(self.movieBottomFrame)
        self.bottomMovieStatText.grid(row=1, column=0, sticky='nsew')
        self.movieBottomFrame.grid_columnconfigure(0, weight=1)
        self.movieBottomFrame.grid_rowconfigure(0, weight=1)

        self.bottomMovieStatText.insert(1.0, "No Movie Stats Loaded\n")
        self.bottomMovieStatText.config(state=tk.DISABLED)
        #endregion
        
        #region TV SHOW TAB
        self.tvShowTab = ttk.Frame(self.main_window)
        self.notebook.add(self.tvShowTab, text="TV Shows")

        self.tvShowTopFrame = ttk.Frame(self.tvShowTab)
        self.tvShowTopFrame.grid(row=0, column=0, sticky="new")
        self.tvShowTab.grid_rowconfigure(0, weight=1)

        self.tvShowBottomFrame = ttk.Frame(self.tvShowTab)
        self.tvShowBottomFrame.grid(row=1, column=0, sticky="sew")
        self.tvShowTab.grid_rowconfigure(1, weight=1)
        self.tvShowTab.grid_columnconfigure(0, weight=1) 

        tvShowScrollbar = tk.Scrollbar(self.tvShowTopFrame)
        tvShowScrollbar.grid(row=0, column=1, sticky='ns')

        self.topTVShowText = tk.Text(self.tvShowTopFrame, yscrollcommand=tvShowScrollbar.set)
        self.topTVShowText.grid(row=0, column=0, sticky='nsew')
        self.tvShowTopFrame.grid_columnconfigure(0, weight=1)
        self.tvShowTopFrame.grid_rowconfigure(0, weight=1)

        tvShowScrollbar.config(command=self.topTVShowText.yview)

        self.topTVShowText.insert(1.0, "No TV Shows Loaded\n")
        self.topTVShowText.config(state=tk.DISABLED)

        self.bottomTVShowStatText = tk.Text(self.tvShowBottomFrame)
        self.bottomTVShowStatText.grid(row=1, column=0, sticky='nsew')
        self.tvShowBottomFrame.grid_columnconfigure(0, weight=1)
        self.tvShowBottomFrame.grid_rowconfigure(0, weight=1)

        self.bottomTVShowStatText.insert(1.0, "No TV Show Stats Loaded\n")
        self.bottomTVShowStatText.config(state=tk.DISABLED)
        #endregion

        #region BOOK TAB
        self.bookTab = ttk.Frame(self.main_window)
        self.notebook.add(self.bookTab, text="Books")

        self.bookTopFrame = ttk.Frame(self.bookTab)
        self.bookTopFrame.grid(row=0, column=0, sticky="new")
        self.bookTab.grid_rowconfigure(0, weight=1)

        self.bookBottomFrame = ttk.Frame(self.bookTab)
        self.bookBottomFrame.grid(row=1, column=0, sticky="sew")
        self.bookTab.grid_rowconfigure(1, weight=1)
        self.bookTab.grid_columnconfigure(0, weight=1) 

        bookScrollbar = tk.Scrollbar(self.bookTopFrame)
        bookScrollbar.grid(row=0, column=1, sticky='ns')

        self.topBookText = tk.Text(self.bookTopFrame, yscrollcommand=bookScrollbar.set)
        self.topBookText.grid(row=0, column=0, sticky='nsew')
        self.bookTopFrame.grid_columnconfigure(0, weight=1)
        self.bookTopFrame.grid_rowconfigure(0, weight=1)

        bookScrollbar.config(command=self.topBookText.yview)

        self.topBookText.insert(1.0, "No Books Loaded\n")
        self.topBookText.config(state=tk.DISABLED)

        self.bottomBookStatText = tk.Text(self.bookBottomFrame)
        self.bottomBookStatText.grid(row=1, column=0, sticky='nsew')
        self.bookBottomFrame.grid_columnconfigure(0, weight=1)
        self.bookBottomFrame.grid_rowconfigure(0, weight=1)

        self.bottomBookStatText.insert(1.0, "No Book Stats Loaded\n")
        self.bottomBookStatText.config(state=tk.DISABLED)
        #endregion
        
        #region SEARCH MOVIES/TV TAB
        self.searchMoviesTab = ttk.Frame(self.main_window)
        self.notebook.add(self.searchMoviesTab, text="Search Movies/TV")
        
        self.searchMoviesTopFrame = ttk.Frame(self.searchMoviesTab)
        self.searchMoviesTopFrame.grid(row=0, column=0, sticky="nesw")
        self.searchMoviesTab.grid_rowconfigure(0, weight=0)
        self.searchMoviesTab.grid_rowconfigure(1, weight=1)
        self.searchMoviesTab.grid_columnconfigure(0, weight=1)
        
        self.typeLabel = ttk.Label(self.searchMoviesTopFrame, text="Type:")
        self.typeCombobox = ttk.Combobox(self.searchMoviesTopFrame, values=["TV Show", "Movie"])
        self.typeCombobox.current(0)
        self.typeLabel.grid(row=0, column=0, sticky="W")
        self.typeCombobox.grid(row=0, column=1, sticky="W")
        
        self.titleLabel = ttk.Label(self.searchMoviesTopFrame, text="Title:")
        self.titleEntry = ttk.Entry(self.searchMoviesTopFrame)
        self.titleLabel.grid(row=1, column=0, sticky="W")
        self.titleEntry.grid(row=1, column=1, sticky="W")

        self.directorLabel = ttk.Label(self.searchMoviesTopFrame, text="Director:")
        self.directorEntry = ttk.Entry(self.searchMoviesTopFrame)
        self.directorLabel.grid(row=2, column=0, sticky="W")
        self.directorEntry.grid(row=2, column=1, sticky="W")

        self.actorLabel = ttk.Label(self.searchMoviesTopFrame, text="Actor:")
        self.actorEntry = ttk.Entry(self.searchMoviesTopFrame)
        self.actorLabel.grid(row=3, column=0, sticky="W")
        self.actorEntry.grid(row=3, column=1, sticky="W")

        self.genreLabel = ttk.Label(self.searchMoviesTopFrame, text="Genre:")
        self.genreEntry = ttk.Entry(self.searchMoviesTopFrame)
        self.genreLabel.grid(row=4, column=0, sticky="W")
        self.genreEntry.grid(row=4, column=1, sticky="W")
        
        self.searchMovieButton = ttk.Button(self.searchMoviesTopFrame, text="Search", command=self.searchShows)
        self.searchMovieButton.grid(row=5, column=0, sticky="W")

        
        # Search results frame
        self.resultsFrame = ttk.Frame(self.searchMoviesTab)
        self.resultsFrame.grid(row=1, column=0, sticky="nsew")
        self.resultsFrame.grid_columnconfigure(0, weight=1)
        self.resultsFrame.grid_rowconfigure(0, weight=1)
        
        # Search Results Scrollbar
        self.resultsScrollbar = tk.Scrollbar(self.resultsFrame)
        self.resultsScrollbar.grid(row=0, column=1, sticky='ns')

        # Search results textbox
        self.resultsText = tk.Text(self.resultsFrame, yscrollcommand=self.resultsScrollbar.set)
        self.resultsText.grid(row=0, column=0, sticky='nsew')
        
        self.resultsText.insert(1.0, "No Search Results\n")
        self.resultsText.config(state=tk.DISABLED)
        
        # Configure the scrollbar
        self.resultsScrollbar.config(command=self.resultsText.yview)
        #endregion

        #region SEARCH BOOKS TAB
        self.searchBookTab = ttk.Frame(self.main_window)
        self.notebook.add(self.searchBookTab, text="Search Books")
        
        self.searchBookTopFrame = ttk.Frame(self.searchBookTab)
        self.searchBookTopFrame.grid(row=0, column=0, sticky="nesw")
        self.searchBookTab.grid_rowconfigure(0, weight=0)
        self.searchBookTab.grid_rowconfigure(1, weight=1)
        self.searchBookTab.grid_columnconfigure(0, weight=1)
        
        self.bookTitleLabel = ttk.Label(self.searchBookTopFrame, text="Title:")
        self.bookTitleEntry = ttk.Entry(self.searchBookTopFrame)
        self.bookTitleLabel.grid(row=0, column=0, sticky="W")
        self.bookTitleEntry.grid(row=0, column=1, sticky="W")

        self.bookAuthorLabel = ttk.Label(self.searchBookTopFrame, text="Author:")
        self.bookAuthorEntry = ttk.Entry(self.searchBookTopFrame)
        self.bookAuthorLabel.grid(row=1, column=0, sticky="W")
        self.bookAuthorEntry.grid(row=1, column=1, sticky="W")

        self.bookPublisherLabel = ttk.Label(self.searchBookTopFrame, text="Publisher:")
        self.bookPublisherEntry = ttk.Entry(self.searchBookTopFrame)
        self.bookPublisherLabel.grid(row=2, column=0, sticky="W")
        self.bookPublisherEntry.grid(row=2, column=1, sticky="W")
        
        self.searchBookButton = ttk.Button(self.searchBookTopFrame, text="Search", command=self.searchBooks)
        self.searchBookButton.grid(row=5, column=0, sticky="W")
        
        self.bookResultsFrame = ttk.Frame(self.searchBookTab)
        self.bookResultsFrame.grid(row=1, column=0, sticky="nsew")
        self.bookResultsFrame.grid_columnconfigure(0, weight=1)
        self.bookResultsFrame.grid_rowconfigure(0, weight=1)
        
        # Search Results Scrollbar
        self.bookResultsScrollbar = tk.Scrollbar(self.bookResultsFrame)
        self.bookResultsScrollbar.grid(row=0, column=1, sticky='ns')

        # Search results textbox
        self.bookResultsText = tk.Text(self.bookResultsFrame, yscrollcommand=self.bookResultsScrollbar.set)
        self.bookResultsText.grid(row=0, column=0, sticky='nsew')

        self.bookResultsText.insert(1.0, "No Search Results\n")
        self.bookResultsText.config(state=tk.DISABLED)
        
        # Configure the scrollbar
        self.bookResultsScrollbar.config(command=self.bookResultsText.yview)
        #endregion

        #region RECOMMENDATIONS TAB
        self.recommendationTab = ttk.Frame(self.main_window)
        self.notebook.add(self.recommendationTab, text="Recommendations")

        self.recommendationsFrame = ttk.Frame(self.recommendationTab)
        self.recommendationsFrame.grid(row=0, column=0, sticky="nesw")
        self.recommendationTab.grid_rowconfigure(0, weight=0)
        self.recommendationTab.grid_rowconfigure(1, weight=1)
        self.recommendationTab.grid_columnconfigure(0, weight=1)
        
        self.recommendationTypeLabel = ttk.Label(self.recommendationsFrame, text="Type:")
        self.recommendationTypeCombobox = ttk.Combobox(self.recommendationsFrame, values=["TV Show", "Movie", "Book"])
        self.recommendationTypeCombobox.current(0)
        self.recommendationTypeLabel.grid(row=0, column=0, sticky="W")
        self.recommendationTypeCombobox.grid(row=0, column=1, sticky="W")
        
        self.recommendationTitleLabel = ttk.Label(self.recommendationsFrame, text="Title:")
        self.recommendationTitleEntry = ttk.Entry(self.recommendationsFrame)
        self.recommendationTitleLabel.grid(row=1, column=0, sticky="W")
        self.recommendationTitleEntry.grid(row=1, column=1, sticky="W")
        
        self.getRecommendationButton = ttk.Button(self.recommendationsFrame, text="Get Recommendation",command=self.getRecommendations)
        self.getRecommendationButton.grid(row=5, column=0, sticky="W")
        
        self.recommendationResultsFrame = ttk.Frame(self.recommendationTab)
        self.recommendationResultsFrame.grid(row=1, column=0, sticky="nsew")
        self.recommendationResultsFrame.grid_columnconfigure(0, weight=1)
        self.recommendationResultsFrame.grid_rowconfigure(0, weight=1)
        
        # Recommendations Scrollbar
        self.recommendationsResultsScrollbar = ttk.Scrollbar(self.recommendationResultsFrame)
        self.recommendationsResultsScrollbar.grid(row=0, column=1, sticky='ns')

        # Recommendations textbox
        self.recommendationsResultsTextbox = tk.Text(self.recommendationResultsFrame, yscrollcommand=self.recommendationsResultsScrollbar.set)
        self.recommendationsResultsTextbox.grid(row=0, column=0, sticky='nsew')

        self.recommendationsResultsTextbox.insert(1.0, "No Recommendations\n")
        self.recommendationsResultsTextbox.config(state=tk.DISABLED)
        
        # Configure the scrollbar
        self.recommendationsResultsScrollbar.config(command=self.recommendationsResultsTextbox.yview)
        #endregion
        
        #region BONUS - RATINGS
        self.ratingsTab = ttk.Frame(self.main_window)
        self.notebook.add(self.ratingsTab, text="Ratings")

        self.ratingsFrame = ttk.Frame(self.ratingsTab)
        self.ratingsFrame.grid(row=0, column=0, sticky="nesw")
        self.ratingsTab.grid_rowconfigure(0, weight=1)  # Make the frame expand with the tab
        self.ratingsTab.grid_columnconfigure(0, weight=1)

        self.generateChartsButton = ttk.Button(self.ratingsFrame, text="Generate Charts", command=self.generate_and_display_charts)
        self.generateChartsButton.grid(row=0, column=0, pady=20, padx=20, sticky="n")  # Place button at the top, center it

        # Set grid weights to make the frame expand
        self.ratingsFrame.grid_rowconfigure(1, weight=1)  # This makes the space below the button expand
        self.ratingsFrame.grid_columnconfigure(0, weight=1)
        #endregion
        
        # BUTTONS
        self.buttonFrame = ttk.Frame(self.main_window)
        self.buttonFrame.pack(side='bottom', fill='x')

        self.loadShowsButton = ttk.Button(self.buttonFrame, text="Load Shows", command=self.loadShows)
        self.loadShowsButton.pack(side='left', padx=120)

        self.loadBooksButton = ttk.Button(self.buttonFrame, text="Load Books", command=self.loadBooks)
        self.loadBooksButton.pack(side='left', padx=60)

        self.loadRecommendationsButton = ttk.Button(self.buttonFrame, text="Load Recommendations", command=self.loadAssociations)
        self.loadRecommendationsButton.pack(side='left', padx=60)

        self.informatoinButton = ttk.Button(self.buttonFrame, text="Information", command=self.creditInfoBox)
        self.informatoinButton.pack(side='left', padx=60)

        self.quitButton = ttk.Button(self.buttonFrame, text="Quit", command=self.main_window.destroy)
        self.quitButton.pack(side='left', padx=60)

        self.notebook.pack(expand=1, fill="both")

        self.main_window.mainloop()

    def generate_and_display_charts(self):
        # Clear the frame content except the button
        try: 
            for widget in self.ratingsFrame.winfo_children():
                if widget != self.generateChartsButton:
                    widget.destroy()

            # Get data
            movie_ratings = self.recc.getMovieRatings()
            tv_show_ratings = self.recc.getTVRatings()

            # Create pie charts
            movie_chart_path = self.create_pie_chart(movie_ratings, "Movie Ratings")
            tv_chart_path = self.create_pie_chart(tv_show_ratings, "TV Show Ratings")

            # Display pie charts on Canvas
            self.display_chart_on_canvas(movie_chart_path, self.ratingsFrame, row=1, column=0)
            self.display_chart_on_canvas(tv_chart_path, self.ratingsFrame, row=1, column=1)
        except Exception as e:
            self.displayError(e)

    def create_pie_chart(self, data, title):
        labels = list(data.keys())
        sizes = list(data.values())
        fig = Figure(figsize=(3.5, 3.5))
        ax = fig.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90, textprops={"fontsize": 6})
        ax.set_title(title, fontsize=12, verticalalignment='bottom')

        # Adjust layout to make room for the title and prevent clipping
        fig.subplots_adjust(top=0.85)
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        
        # Save the figure to a temporary path
        temp_path = f"temp_{title.replace(' ', '_').lower()}.png"
        fig.savefig(temp_path, bbox_inches='tight')
        plt.close(fig)  # Close the figure to free memory
        return temp_path
    
    def display_chart_on_canvas(self, image_path, frame, row, column):
        canvas_width = 350
        canvas_height = 350
        canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height)
        canvas.grid(row=row, column=column, sticky="nsew")
        frame.grid_rowconfigure(row, weight=1)
        frame.grid_columnconfigure(column, weight=1)

        tk_img = tk.PhotoImage(file=image_path)
        canvas.create_image(canvas_width / 2, canvas_height / 2, image=tk_img)
        canvas.image = tk_img  # Keep a reference!

        # Optionally remove the image file after displaying
        os.remove(image_path)

    def loadShows(self):
        """
        This function displays the shows and their statistics in the GUI.
        """
        try: 
            self.recc.loadShows()

            # MOVIES
            self.topMoiveText.config(state=tk.NORMAL)
            self.topMoiveText.delete(1.0, tk.END)

            movieTitleLen, movieList = self.recc.getMovieList()
            movieTitles = [movieList[i]["title"] for i in range(len(movieList))]
            movieRuntime = [movieList[i]["runtime"] for i in range(len(movieList))]

            self.topMoiveText.insert(1.0, f"{'Title':<{movieTitleLen}} Runtime\n")
            for i in range(len(movieTitles)):
                self.topMoiveText.insert(tk.END, f"{movieTitles[i]:<{movieTitleLen}} {movieRuntime[i]}\n")
            self.topMoiveText.config(state=tk.DISABLED)

            ratingPercentages, avgDuration, most_common_directors, most_common_actors, most_common_genres = self.recc.getMovieStats()

            self.bottomMovieStatText.config(state=tk.NORMAL)
            self.bottomMovieStatText.delete(1.0, tk.END)

            self.bottomMovieStatText.insert(1.0, "Ratings: \n")
            for rating in ratingPercentages:
                self.bottomMovieStatText.insert(tk.END, rating + "\n")
            
            self.bottomMovieStatText.insert(tk.END, f"\nAverage Movie Duration: {avgDuration} \n")
            self.bottomMovieStatText.insert(tk.END, f"\nMost Common Director: {most_common_directors} \n")
            self.bottomMovieStatText.insert(tk.END, f"\nMost Common Actor: {most_common_actors} \n")
            self.bottomMovieStatText.insert(tk.END, f"\nMost Frequent Genre: {most_common_genres} \n")
            self.bottomMovieStatText.config(state=tk.DISABLED)      


            # TV SHOWS
            self.topTVShowText.config(state=tk.NORMAL)
            self.topTVShowText.delete(1.0, tk.END)
            
            tvShowTitleLen, tvShowList = self.recc.getTVList()
            tvShowTitles = [tvShowList[i]["title"] for i in range(len(tvShowList))]
            tvShowSeasons = [tvShowList[i]["seasons"] for i in range(len(tvShowList))]

            self.topTVShowText.insert(1.0, f"{'Title':<{tvShowTitleLen}} Seasons\n")
            for i in range(len(tvShowTitles)):
                self.topTVShowText.insert(tk.END, f"{tvShowTitles[i]:<{tvShowTitleLen}} {tvShowSeasons[i]}\n")
            self.topTVShowText.config(state=tk.DISABLED)

            ratingPercentages, avgDuration, most_common_actors, most_common_genres = self.recc.getTVStats()

            self.bottomTVShowStatText.config(state=tk.NORMAL)
            self.bottomTVShowStatText.delete(1.0, tk.END)

            self.bottomTVShowStatText.insert(1.0, "Ratings: \n")
            for rating in ratingPercentages:
                self.bottomTVShowStatText.insert(tk.END, rating + "\n")

            self.bottomTVShowStatText.insert(tk.END, f"\nAverage TV Show Duration: {avgDuration} \n")
            self.bottomTVShowStatText.insert(tk.END, f"\nMost Common Actor: {most_common_actors} \n")
            self.bottomTVShowStatText.insert(tk.END, f"\nMost Frequent Genre: {most_common_genres} \n")
            self.bottomTVShowStatText.config(state=tk.DISABLED)

        except Exception as e:
            self.displayError(e)
            self.loadShows()
        

    def loadBooks(self):
        """
        This function displays the books and their statistics in the GUI.
        """
        try:
            self.recc.loadBooks()

            self.topBookText.config(state=tk.NORMAL)
            self.topBookText.delete(1.0, tk.END)
            
            bookTitleLen, bookList = self.recc.getBookList()
            bookTitles = [bookList[i]["title"] for i in range(len(bookList))]
            bookAuthors = [bookList[i]["authors"] for i in range(len(bookList))]

            self.topBookText.insert(1.0, f"{'Title':<{bookTitleLen}} Author(s)\n")
            for i in range(len(bookTitles)):
                self.topBookText.insert(tk.END, f"{bookTitles[i]:<{bookTitleLen}} {bookAuthors[i]}\n")
            self.topBookText.config(state=tk.DISABLED)

            avgPages, most_common_authors, most_common_publishers = self.recc.getBookStats()

            self.bottomBookStatText.config(state=tk.NORMAL)
            self.bottomBookStatText.delete(1.0, tk.END)

            self.bottomBookStatText.insert(tk.END, f"\nAverage Page Count: {avgPages} \n")
            self.bottomBookStatText.insert(tk.END, f"\nMost Profilic Author: {most_common_authors} \n")
            self.bottomBookStatText.insert(tk.END, f"\nMost Profilic Publisher: {most_common_publishers} \n")
            self.bottomBookStatText.config(state=tk.DISABLED)
        except Exception as e:
            self.displayError(e)
            self.loadBooks()
    
    def loadAssociations(self):
        """
        This function loads the associations between the shows, books, and recommendations.
        """
        try:
            self.recc.loadAssociations()
        except Exception as e:
            self.displayError(e)
            self.loadAssociations()
        return
    
    def creditInfoBox(self):
        # return a showinfo messagebox with information about the program
        tk.messagebox.showinfo("Information", "Bishawjit Saha and Sparsh Oza \nThis project was completed 05/04/2024")

    def searchShows(self):
        # searches for TV shows or movies based on the user's input in the GUI.
        # populates the resultsText textbox with the title, director, actor, and genre of each item found in the search results.
        try: 
            types = ["TV Show", "Movie"]
            searchType = types[self.typeCombobox.current()]
            searchTitle = self.titleEntry.get()
            searchDirector = self.directorEntry.get()
            searchActor = self.actorEntry.get()
            searchGenre = self.genreEntry.get()
            self.resultsText.delete(1.0, tk.END)
            searchResult = self.recc.searchTVMovies(searchType, searchTitle, searchDirector, searchActor, searchGenre)

            if searchResult == []:
                self.resultsText.insert(1.0, "No Results Found\n")
                self.resultsText.config(state=tk.DISABLED)
                return

            self.resultsText.config(state=tk.NORMAL)
            self.resultsText.delete(1.0, tk.END)

            titleLen = max(len(item['title']) for item in searchResult)
            directorLen = max(len("\\".join(item["director"])) for item in searchResult)
            actorLen = max(len("\\".join(item["actor"])) for item in searchResult)

            # Check each value
            if directorLen == 0 or directorLen is None:
                directorLen = 10
            
            
            self.resultsText.insert(1.0, f"{'Title':<{titleLen}} {'Director':<{directorLen}} {'Actor':<{actorLen}} {'Genre'}\n")
            for item in searchResult:
                title = item["title"]
                director = "\\".join(item["director"])
                actor = "\\".join(item["actor"])
                genre = "\\".join(item["genre"])
                self.resultsText.insert(tk.END, f"{title:<{titleLen}} {director:<{directorLen}} {actor:<{actorLen}} {genre}\n")
            self.resultsText.config(state=tk.DISABLED)
        except Exception as e:
            self.displayError(e)
        return
    
    def searchBooks(self):        
        # retrieves books based on the title, author, and publisher entered in the GUI
        # populates the bookResultsText with the details of each book found in the search results
        try:
            searchTitle = self.bookTitleEntry.get()
            searchAuthor = self.bookAuthorEntry.get()
            searchPublisher = self.bookPublisherEntry.get()
            self.bookResultsText.delete(1.0, tk.END)
            searchResult = self.recc.searchBooks(searchTitle, searchAuthor, searchPublisher)
            
            if searchResult == []:
                self.bookResultsText.insert(1.0, "No Results Found\n")
                self.bookResultsText.config(state=tk.DISABLED)
                return
            
            self.bookResultsText.config(state=tk.NORMAL)
            self.bookResultsText.delete(1.0, tk.END)
            
            titleLen = max(len(item["title"]) for item in searchResult)
            authorLen = max(len("\\".join(item["author"])) for item in searchResult)

            
            self.bookResultsText.insert(1.0, f"{'Title':<{titleLen}} {'Author':<{authorLen}} {'Publisher'}\n")
            for item in searchResult:
                title = item["title"]
                author = "\\".join(item["author"])
                publisher = item["publisher"]
                
                self.bookResultsText.insert(tk.END, f"{title:<{titleLen}} {author:<{authorLen}} {publisher}\n")
            self.bookResultsText.config(state=tk.DISABLED)
        except Exception as e:
            self.displayError(e)
        return
    
    def getRecommendations(self):
        #retrieves recommendations based on the selected type and title from the GUI
        #populates the recommendationsResultsTextbox with the details of each recommended item.
        try:
            types = ["TV Show", "Movie", "Book"]
            recType = types[self.recommendationTypeCombobox.current()]
            recTitle = self.recommendationTitleEntry.get()
            recResult = self.recc.getRecommendations(recType, recTitle)

            if recResult == []:
                self.recommendationsResultsTextbox.insert(1.0, "No Recommendations Found\n")
                self.recommendationsResultsTextbox.config(state=tk.DISABLED)
                return
            
            self.recommendationsResultsTextbox.config(state=tk.NORMAL)
            self.recommendationsResultsTextbox.delete(1.0, tk.END)

            for item in recResult:
                self.recommendationsResultsTextbox.insert(tk.END, "Title:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['Title']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "Author:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{'\\'.join(item['Author'])}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "Average Rating:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['Average Rating']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "ISBN:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['ISBN']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "ISBN13:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['ISBN13']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "Language Code:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['Language Code']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "Pages:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['Pages']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "Rating Count:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['Rating Count']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "Publication Date:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['Publication Date']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "Publisher:\n")
                self.recommendationsResultsTextbox.insert(tk.END, f"{item['Publisher']}\n")
                self.recommendationsResultsTextbox.insert(tk.END, "\n*************************\n\n")
            
            self.recommendationsResultsTextbox.config(state=tk.DISABLED)
        except Exception as e:
            self.displayError(e)
        return
    
    def displayError(self, error):
        """
        This function displays an error message in a messagebox.
        """
        tk.messagebox.showerror("Error", error)

if __name__ == "__main__":
    app = RecommenderGUI()