# Description:

import Recommender
import tkinter as tk
from tkinter import ttk

class RecommenderGUI:
    def __init__(self):
        self.recc = Recommender.Recommender()

        self.main_window = tk.Tk()
        self.main_window.title("Media Recommender")
        self.main_window.geometry("1200x800")
        self.notebook = ttk.Notebook(self.main_window)

        # MOVIE TAB
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
        
        # TV SHOW TAB
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

        # BOOK TAB
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

        # SEARCH MOVIES/TV TAB
        self.searchTVmovies = ttk.Frame(self.main_window)
        self.notebook.add(self.searchTVmovies, text="Search Movies/TV")


        # SEARCH BOOKS TAB
        self.bookSearch = ttk.Frame(self.main_window)
        self.notebook.add(self.bookSearch, text="Search Books")


        # RECOMMENDATIONS TAB
        self.reccomendation = ttk.Frame(self.main_window)
        self.notebook.add(self.reccomendation, text="Recommendations")


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

    def loadShows(self):
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

    def loadBooks(self):
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
    
    def loadAssociations(self):
        # TODO
        return
    
    def creditInfoBox(self):
        # return a showinfo messagebox with information about the program
        tk.messagebox.showinfo("Information", "Bishawjit Saha and Sparsh Oza \nThis project was completed 05/04/2024")

    def searchShows(self):
        # TODO
        return
    
    def searchBooks(self):
        # TODO
        return
    
    def getRecommendations(self):
        # TODO
        return

if __name__ == "__main__":
    app = RecommenderGUI()