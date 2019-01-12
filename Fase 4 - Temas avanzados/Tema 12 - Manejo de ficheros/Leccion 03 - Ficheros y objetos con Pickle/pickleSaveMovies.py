from io import open
from Movie import Movie
import pickle

# Now let's practice to save arrays, dictionaries or objects in binary files, this is very easy to use if you
# use pickle. Pickle, is a library that allows you to dump python data to files and load in easy steps. Let's see!
# In this example we create an array of movies and dump the array to a binary file.

movies = [
    Movie("El Padrino", 1985, "Drama"), 
    Movie("Star Wars The Force Unleashed", 2010, "Fiction"), 
    Movie("American Pie 2", 2003, "Sex and Comedy")]

file = open("movies.pckl", "wb")
pickle.dump(movies, file)
file.close()