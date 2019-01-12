from io import open
from Movie import Movie
import pickle

# Now let's practice to save arrays, dictionaries or objects in binary files, this is very easy to use if you
# use pickle. Pickle, is a library that allows you to dump python data to files and load in easy steps. Let's see!
# In this example load from a binary file an array of Movie objects

file = open("movies.pckl", "rb")
movies = pickle.load(file)

for movie in movies:
    print(movie)

file.close()
