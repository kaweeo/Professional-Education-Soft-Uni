def movie_organizer(*movie_data):
    movies_dict = {}
    result = ""

    for movie, genre in movie_data:
        if genre not in movies_dict.keys():
            movies_dict[genre] = []
        movies_dict[genre].append(movie)

    for value in movies_dict.values():
        value.sort()

    sorted_movies_dict = dict(sorted(movies_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for k, v in sorted_movies_dict.items():
        result += f"{k} - {len(v)}\n"
        for movie in v:
            result += f"* {movie}\n"

    return result


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