"""Media module - holds Movie class """
import webbrowser

class Movie(object):
    """Holds movie properties and methods """
    # Constructor, initializes instance variables
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """ Opens up trailer"""
        webbrowser.open(self.trailer_youtube_url)
