def movie_organizer(*args):
    movie_groups = {}

    for name, movie_genre in args:
        if movie_genre not in movie_groups:
            movie_groups[movie_genre] = []
        movie_groups[movie_genre].append(name)

    result = ''
    
    sorted_movies = sorted(movie_groups.items(), key = lambda kvp: (-len(kvp[1]), kvp[0]))
    for genre, names in sorted_movies:
        result += f'{genre} - {len(movie_groups[genre])}\n'
        sorted_movies = sorted(names)
        for movie_name in sorted_movies:    
            result += f'* {movie_name}\n'
    return result[:-1]


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))