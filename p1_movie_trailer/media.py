import webbrowser

class Movie():
	""" This class provides ways to store movie info, based on the 
	 Programming Foundations with Python course.
	""" 
	VALID_RATINGS=['G','PG','PG-13','R']
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		""" Initializes the instance with basic information of the movie """
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
	def show_trailer(self):
		""" This method will launch a new web browser windows to display
		The trailer of the instance
		"""
		webbrowser.open(self.
		railer_youtube_url)