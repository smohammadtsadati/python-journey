movies = ["inception", "interstellar", "the matrix"]

print("My favorite ,ovies are: ")
for movie in movies:
	print(movie)

new_movie = input("Enter another movie you like: ")
movies.append(new_movie)

print("Updated list: ")
print(movies)