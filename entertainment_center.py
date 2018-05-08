import fresh_tomatoes
import media

# making instances of movies to show
cinema_paradiso = media.Movie("Cinema Paradiso",
                              "https://upload.wikimedia.org/wikipedia/en/8/86/CinemaParadiso.jpg",
                              "https://www.youtube.com/watch?v=C2-GX0Tltgw")

leon = media.Movie("Leon", "https://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",
                   "https://www.youtube.com/watch?v=Dc1KzpMnuX0")

shawshank = media.Movie("Shawshank Redemption",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

life_is_beautiful = media.Movie("Life is Beaufitul",
                                "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
                                "https://www.youtube.com/watch?v=pAYEQP8gx3w")

children_of_heaven = media.Movie("Children of Heaven",
                                 "https://upload.wikimedia.org/wikipedia/en/f/f7/Children_of_heaven.jpg",
                                 "https://www.youtube.com/watch?v=dqxvZeQsVzY")

look_of_silence = media.Movie("Look of Silence",
                              "https://upload.wikimedia.org/wikipedia/en/7/77/The_Look_of_Silence_%282014_film%29.jpg",
                              "https://www.youtube.com/watch?v=aA_ZHAs4M9k")

movies = [cinema_paradiso, leon, shawshank, life_is_beautiful, children_of_heaven, look_of_silence]

# generate html file from movies and open in new tab
fresh_tomatoes.open_movies_page(movies)
