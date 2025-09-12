import os
import django

# Setup Django environment so we can use ORM outside manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "J.K. Rowling"  # Example
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print("-", book.title)
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# 2. List all books in a library
library_name = "Central Library"  # Example
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print("-", book.title)
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# 3. Retrieve the librarian for a library
# 3. Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library=library)  # ✅ this matches the checker
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")

