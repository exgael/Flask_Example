import requests
import random

# URL de l'API
API_URL = "http://localhost:8000/books"

# Données de livres
books_data = [
    {"title": "Les Misérables", "author": "Victor Hugo", "published_year": 1862},
    {"title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry", "published_year": 1943},
    {"title": "1984", "author": "George Orwell", "published_year": 1949},
    {"title": "Le Seigneur des Anneaux", "author": "J.R.R. Tolkien", "published_year": 1954},
    {"title": "Le Comte de Monte-Cristo", "author": "Alexandre Dumas", "published_year": 1844},
    {"title": "Moby-Dick", "author": "Herman Melville", "published_year": 1851},
    {"title": "L'Odyssée", "author": "Homère", "published_year": -800},
    {"title": "Le Grand Gatsby", "author": "F. Scott Fitzgerald", "published_year": 1925},
    {"title": "Guerre et Paix", "author": "Léon Tolstoï", "published_year": 1869},
    {"title": "Anna Karénine", "author": "Léon Tolstoï", "published_year": 1877}
]

def post_book(book):
    response = requests.post(API_URL, json=book)
    if response.status_code == 201:
        print(f"Le livre '{book['title']}' a été ajouté avec succès.")
    else:
        print(f"Échec de l'ajout du livre '{book['title']}'. Réponse: {response.status_code}")

if __name__ == "__main__":
    for book in books_data:
        post_book(book)
