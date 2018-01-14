"""Media module - holds Movie class """
import webbrowser


class Movie(object):
    """ Class Movie describing the attributes of movie.

        Arguments:
            movie_title {str} -- Movie title
            movie_storyline {str} -- Movie story line
            movie_poster {str} -- Movie Poster
            movie_trailer {str} -- Movie Trailer

        Attributes:
            title {str} -- Movie title
            storyline {str} -- Movie story line
            poster_image_url {str} -- Movie Poster
            trailer_youtube_url {str} -- Movie Trailer

        Methods:
            show_trailer: Opens youtube movie trailer url in browser
    """

    def __init__(
            self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """Opens movie trailer in browser

        Returns: None.
        """
        webbrowser.open(self.trailer_youtube_url)
