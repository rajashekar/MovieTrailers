""" Create movie objects and calls fresh_tomatoes.open_movies_page to generate html """
import media
import fresh_tomatoes

# Creating movie objects
TOY_STORY = media.Movie("Toy Story",
                        "A story of Toy",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
AVATAR = media.Movie("Avatar",
                     "A marine on alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
FIGHTCLUB = media.Movie("Fight Club",
                        "Mischief. Mayhem. Soap.",
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")
VFORVENDETTA = media.Movie("V for Vendetta",
                           "People should not be afraid of their governments. Governments \
                           should be afraid of their people.",
                           "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
                           "https://www.youtube.com/watch?v=jS4sVTDAsJ4")
EVERYTHINGISILLUMINATED = media.Movie("Everything Is Illuminated",
                                      "Leave Normal Behind.",
                                      "https://upload.wikimedia.org/wikipedia/en/2/27/Everything_Is_Illuminated_film.jpg",
                                      "https://www.youtube.com/watch?v=l-hCtlNM32M")
CONTACT = media.Movie("Contact",
                      "If it's just us, it seems like an awful waste of space.",
                      "https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
                      "https://www.youtube.com/watch?v=SRoj3jK37Vc")

# Keeping all above objects in a list
MOVIES = [TOY_STORY, AVATAR, FIGHTCLUB, VFORVENDETTA, EVERYTHINGISILLUMINATED, CONTACT]
fresh_tomatoes.open_movies_page(MOVIES)
