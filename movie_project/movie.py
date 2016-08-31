import movie_class
import movie_website

iron_man = movie_class.Movie(
    "Iron Man",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=8hYlB38asDY")

incredible_hulk = movie_class.Movie(
    "The Incredible Hulk",
    "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
    "https://www.youtube.com/watch?v=xbqNb2PFKKA")

iron_man2 = movie_class.Movie(
    "Iron Man 2",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
    "https://www.youtube.com/watch?v=BoohRoVA9WQ")

thor = movie_class.Movie(
    "Thor", "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
    "https://www.youtube.com/watch?v=JOddp-nlNvQ")

captain_america = movie_class.Movie(
    "Captain America",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
    "https://www.youtube.com/watch?v=JerVrbLldXw")

avengers = movie_class.Movie(
    "The Avengers",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

iron_man3 = movie_class.Movie(
    "Iron Man 3",
    "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=YLorLVa95Xo")

thor_dark_world = movie_class.Movie(
    "Thor: The Dark World",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
    "https://www.youtube.com/watch?v=npvJ9FTgZbM")

captain_america_winter_soldier = movie_class.Movie(
    "Captain America: The Winter Soldier",
    "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
    "https://www.youtube.com/results?search_query=winter+soldier+trailer")

guardians_galaxy = movie_class.Movie(
    "Guardians of the Galaxy",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
    "https://www.youtube.com/watch?v=d96cjJhvlMA")

age_of_ultron = movie_class.Movie(
    "Avengers: Age of Ultron",
    "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
    "https://www.youtube.com/watch?v=JAUoeqvedMo")

ant_man = movie_class.Movie(
    "Ant Man",
    "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
    "https://www.youtube.com/watch?v=pWdKf3MneyI")

civil_war = movie_class.Movie(
    "Captain America: Civil War",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
    "https://www.youtube.com/watch?v=dKrVegVI0Us")

doctor_strange = movie_class.Movie(
    "Doctor Strange",
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
    "https://www.youtube.com/watch?v=HSzx-zryEgM")

movies = [iron_man, incredible_hulk, iron_man2, thor, captain_america,
          avengers, iron_man3, thor_dark_world, captain_america_winter_soldier,
          guardians_galaxy, age_of_ultron, ant_man, civil_war, doctor_strange]
movie_website.open_movies_page(movies)
