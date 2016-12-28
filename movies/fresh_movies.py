import media
import fresh_tomatoes


riverdale=media.Movie("Riverdale","Storyline",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwOTc0MjAzNl5BMl5BanBnXkFtZTgwNDU2NTc4MDI@._V1_UY268_CR16,0,182,268_AL__QL50.jpg",
                      "https://www.youtube.com/watch?v=jMlJ7FTk35c")

blade_runner= media.Movie("Blade Runner 2049","Storyline",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BNDIxMDE3NzcxN15BMl5BanBnXkFtZTgwNzQyMzE5MDI@._V1_UX156_CR0,0,156,231_AL_.jpg",
                                "https://www.youtube.com/watch?v=S_JAMRKzEHs")

john_wick = media.Movie("John Wick Chapter:2","Storyline",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxMzc4MTkwOF5BMl5BanBnXkFtZTgwOTE5MDcyMDI@._V1_UY231_CR3,0,156,231_AL_.jpg",
                                  "https://www.youtube.com/watch?v=XGk2EfbD_Ps")

a_monster_calls= media.Movie("A Monster Calls","Storyline",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1OTA5OTkyNV5BMl5BanBnXkFtZTgwODMwNDU5OTE@._V1_UX156_CR0,0,156,231_AL_.jpg",
                             "https://www.youtube.com/watch?v=R2Xbo-irtBA")

rogue_one = media.Movie("Rogue One","Storyline",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_UX156_CR0,0,156,231_AL_.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

assasins_creed = media.Movie("Assasin's Creed","Storyline",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BNzE1OTczNTc1OF5BMl5BanBnXkFtZTgwMzgyMDI3MDI@._V1_UX156_CR0,0,156,231_AL_.jpg",
                             "https://www.youtube.com/watch?v=C2e6Oruy_fA")

snatched = media.Movie("Snatched","Storyline",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BODI1NDM5MjctODEyYy00MmQ3LWIwY2YtYjliZDExYmFhNWNiL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjI5NTU5MjE@._V1_UY268_CR16,0,182,268_AL__QL50.jpg",
                       "https://www.youtube.com/watch?v=w0YJcwomapQ")

spiderman_homecoming = media.Movie("Spider-Man: Homecoming","Storyline",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BNDUzOTE5OTk1NF5BMl5BanBnXkFtZTgwNzgwNzA4MDI@._V1_UX156_CR0,0,156,231_AL_.jpg",
                                   "https://www.youtube.com/watch?v=rk-dF1lIbIg")

transformers_last_knight=media.Movie("Transformers: The Last Knight",
                                      "Plot is unknown.",
                                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMwMzM4NTE5OV5BMl5BanBnXkFtZTgwMTAwNDU4MDI@._V1_UX156_CR0,0,156,231_AL_.jpg",
                                     "https://www.youtube.com/watch?v=AntcyqJ6brc")

fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them","Storyline",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxOTM1OTI4MV5BMl5BanBnXkFtZTgwODE5OTYxMDI@._V1_UX156_CR0,0,156,231_AL_.jpg",
                               "https://www.youtube.com/watch?v=0_DNCfYDWqw")

gotg2= media.Movie("Guardians of the Galaxy Vol.2",
                   "A sequel to the Guardians of the Galaxy",
                   "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                   "https://www.youtube.com/watch?v=pr7tDrwQ3t8")

pirates_of_the_carribean = media.Movie("Pirates of the Caribbean: Dead Men Tell No Tale",
                                       "Captain Jack Sparrow searches for the trident of Poseidon.",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BNDY3MDY4MDc3MV5BMl5BanBnXkFtZTgwMTU0MzEyMDI@._V1_UY231_CR3,0,156,231_AL_.jpg",
                                       "https://www.youtube.com/watch?v=1xo3af_6_Jk")

movies =[riverdale,blade_runner,john_wick,a_monster_calls,rogue_one,assasins_creed,snatched,spiderman_homecoming,transformers_last_knight,fantastic_beasts,gotg2,pirates_of_the_carribean]

fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)


