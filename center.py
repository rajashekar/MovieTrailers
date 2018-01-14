import media
import fresh_tomatoes

# Creating movie objects
toy_story = media.Movie("Toy Story",
                        "A story of Toy",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                        "A marine on alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
fightclub = media.Movie("Fight Club",
                        "Mischief. Mayhem. Soap.",
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")
vforvendetta = media.Movie("V for Vendetta",
                           "People should not be afraid of their governments. Governments should be afraid of their people.",
                           "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
                           "https://www.youtube.com/watch?v=jS4sVTDAsJ4")
everythingisilluminated = media.Movie("Everything Is Illuminated",
                                      "Leave Normal Behind.",
                                      "https://upload.wikimedia.org/wikipedia/en/2/27/Everything_Is_Illuminated_film.jpg",
                                      "https://www.youtube.com/watch?v=l-hCtlNM32M")
contact = media.Movie("Contact",
                      "If it's just us, it seems like an awful waste of space.",
                      "https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
                      "https://www.youtube.com/watch?v=SRoj3jK37Vc")

# Keeping all above objects in a list
movies = [toy_story, avatar, fightclub, vforvendetta, everythingisilluminated, contact]
fresh_tomatoes.open_movies_page(movies)
