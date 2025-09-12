# CRUD Operations for Book Model

This file documents all CRUD operations performed on the `Book` model in the Django shell.

---

## 1. Create

```python
from bookshelf.models import Book

# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
# Output: <Book: 1984 by George Orwell>
2. Retrieve
python
Copy code
# Retrieve all books
books = Book.objects.all()
books
# Output: <QuerySet [<Book: 1984 by George Orwell>]>

# Retrieve specific book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)
3. Update
python
Copy code
# Update book title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
book = Book.objects.get(author="George Orwell")
book.title
# Output: 'Nineteen Eighty-Four'
4. Delete
python
Copy code
# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>