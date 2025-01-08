movies = [
    {"title": "Inception", "genre": "Sci-Fi", "director": "Christopher Nolan"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"},
    {"title": "Interstellar", "genre": "Sci-Fi", "director": "Christopher Nolan"},
    {"title": "The Matrix", "genre": "Sci-Fi", "director": "Lana Wachowski, Lilly Wachowski"},
    {"title": "Titanic", "genre": "Romance", "director": "James Cameron"},
    {"title": "The Notebook", "genre": "Romance", "director": "Nick Cassavetes"},
    {"title": "Gladiator", "genre": "Action", "director": "Ridley Scott"},
    {"title": "Avatar", "genre": "Sci-Fi", "director": "James Cameron"},
]
def recommend_movies(user_genre):
    recommendations = []
    for movie in movies:
        if movie["genre"].lower() == user_genre.lower():
            recommendations.append(movie["title"])
    return recommendations  # Ensure this line is properly indented
user_input = input("Enter your preferred genre (e.g., Sci-Fi, Action, Romance): ")
recommended_movies = recommend_movies(user_input)
if recommended_movies:
    print("\nRecommended Movies:")
    for movie in recommended_movies:
        print(f"- {movie}")
else:
    print("No recommendations available for this genre.")
