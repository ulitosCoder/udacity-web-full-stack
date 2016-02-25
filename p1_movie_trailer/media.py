import webbrowser


class Movie():

    """ This class provides ways to store movie info, based on the
     Programming Foundations with Python course.
    """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date=None):
        """Creates a new instance of moive

        Initializes the instance with basic information of the movie

        Args:
                movie_title: Movie title
                movie_storyline: Main plot of the movie
                poster_image: a URL to the poster image
                trailer_youtube: a URL to the movie trailer in YouTube
                release_date: Optional argument, release date of the Movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    def fullTitle(self):
        """ Returns a full title for the Movie

        If the Movie instance includes a release date appends it at the end of
        the main title in parenthesis

        Returns:
                Full Movie title, e.g.

                "Toy Story (1995)"
                or
                "Avatar"

        """
        full_title = self.title
        if(self.release_date is not None):
            full_title = full_title + " (%s)" % self.release_date

        return full_title

    def show_trailer(self):
        """ This method will launch a new web browser window to display
        the YouTube trailer of this Movie instance
        """
        webbrowser.open(self.trailer_youtube_url)
