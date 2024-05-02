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

        self.movieTab = ttk.Frame(self.main_window)
        self.notebook.add(self.movieTab, text="Movies")

        self.topFrame = ttk.Frame(self.movieTab)
        self.topFrame.grid(row=0, column=0, sticky="new")
        self.movieTab.grid_rowconfigure(0, weight=1)

        self.bottomFrame = ttk.Frame(self.movieTab)
        self.bottomFrame.grid(row=1, column=0, sticky="sew")
        self.movieTab.grid_rowconfigure(1, weight=1)
        self.movieTab.grid_columnconfigure(0, weight=1) 

        scrollbar = tk.Scrollbar(self.topFrame)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.topMoiveText = tk.Text(self.topFrame, yscrollcommand=scrollbar.set)
        self.topMoiveText.grid(row=0, column=0, sticky='nsew')
        self.topFrame.grid_columnconfigure(0, weight=1)
        self.topFrame.grid_rowconfigure(0, weight=1)

        scrollbar.config(command=self.topMoiveText.yview)

        self.topMoiveText.insert(1.0, "No Movies Loaded\n")
        self.topMoiveText.config(state=tk.DISABLED)

        self.bottomMovieStatText = tk.Text(self.bottomFrame)
        self.bottomMovieStatText.grid(row=1, column=0, sticky='nsew')
        self.bottomFrame.grid_columnconfigure(0, weight=1)
        self.bottomFrame.grid_rowconfigure(0, weight=1)

        self.bottomMovieStatText.insert(1.0, "No Movie Stats Loaded\n")
        self.bottomMovieStatText.config(state=tk.DISABLED)
        
        self.tvShowTab = ttk.Frame(self.main_window)
        self.notebook.add(self.tvShowTab, text="TV Shows")

        self.bookTab = ttk.Frame(self.main_window)
        self.notebook.add(self.bookTab, text="Books")

        self.searchTVmovies = ttk.Frame(self.main_window)
        self.notebook.add(self.searchTVmovies, text="Search Movies/TV")

        self.searchBooks = ttk.Frame(self.main_window)
        self.notebook.add(self.searchBooks, text="Search Books")

        self.reccomendation = ttk.Frame(self.main_window)
        self.notebook.add(self.reccomendation, text="Recommendations")

        self.buttonFrame = ttk.Frame(self.main_window)
        self.buttonFrame.pack(side='bottom', fill='x')

        self.loadShowsButton = ttk.Button(self.buttonFrame, text="Load Shows", command=self.loadShows)
        self.loadShowsButton.pack(side='left', padx=120)

        self.loadBooksButton = ttk.Button(self.buttonFrame, text="Load Books", command=self.loadBooks)
        self.loadBooksButton.pack(side='left', padx=60)

        self.loadRecommendationsButton = ttk.Button(self.buttonFrame, text="Load Recommendations", command=self.loadRecommendations)
        self.loadRecommendationsButton.pack(side='left', padx=60)

        self.informatoinButton = ttk.Button(self.buttonFrame, text="Information", command=self.information)
        self.informatoinButton.pack(side='left', padx=60)

        self.quitButton = ttk.Button(self.buttonFrame, text="Quit", command=self.main_window.destroy)
        self.quitButton.pack(side='left', padx=60)

        self.notebook.pack(expand=1, fill="both")

        self.main_window.mainloop()

    def loadShows(self):
        self.recc.loadShows()
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

    def loadBooks(self):
        return
    
    def loadRecommendations(self):
        return
    
    def information(self):
        return

if __name__ == "__main__":
    app = RecommenderGUI()