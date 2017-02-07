class Movie:
    """Stores movies information

   This class contains basic movie information

   Attributes:
       movie_title: A String indicating the movie title.
       movie_storyline: A String indicating the movie storyline.
       poster_image: A String that holds poster's image url.
       trailer_youtube: A String that holds a link to the youtube trailer of the movie.
   """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Inits Movie class with basic movie information."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
