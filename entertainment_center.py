import fresh_tomatoes
import media

# Creates instances of the Movie class
toy_story = media.Movie("Toy story",
                        "A story of a boy with toys",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

tangled = media.Movie("Tangled",
                      "Rapunzel with long hair",
                      "https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg",
                      "https://www.youtube.com/watch?v=ip_0CFKTO9E")

up = media.Movie("Up",
                 "Seventy-eight year old Carl Fredricksen travels with balloons",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_(2009_film).jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

eurotrip = media.Movie("Eurotrip",
                       """Dumped by his girlfriend, a high school grad decides
                       to embark on an overseas adventure in Europe with his friends.""",
                       "http://www.stfimages.in/images/2013/07/03/JVxh27H.jpg",
                       "https://www.youtube.com/watch?v=-_Eu0X3B6OM")

stardust = media.Movie("Stardust",
                       """"On a magical land, a young man makes a promise to his beloved
                       that he'll retrieve a fallen star.""",
                       "http://pics.filmaffinity.com/stardust-983044080-large.jpg",
                       "https://www.youtube.com/watch?v=fkHnumjuHL8")

twelve_years_slave = media.Movie("Twelve Years Slave",
                                 "A free black man from upstate New York, is abducted and sold into slavery.",
                                 "https://upload.wikimedia.org/wikipedia/en/5/5c/12_Years_a_Slave_film_poster.jpg",
                                 "https://www.youtube.com/watch?v=z02Ie8wKKRg")
# Create a list of movie objects
movies = [toy_story, tangled, up, eurotrip, stardust, twelve_years_slave]
# Initializes the movie page of the fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
