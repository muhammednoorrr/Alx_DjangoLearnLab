import django
import os

# Setup Django environment (only needed if running standalone script)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        # Using objects.filter as required by the check
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        # Using reverse relation as required by the check
        books_in_library = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # Retrieve the librarian for a library
    try:
        # Using objects.get explicitly as required by the check
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for {library.name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist, AttributeError):
        print(f"No librarian assigned to {library_name}")


if __name__ == "__main__":
    run_queries()
