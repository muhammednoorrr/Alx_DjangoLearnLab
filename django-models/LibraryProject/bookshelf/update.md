# Update Operation

```python
book.title = "Nineteen Eighty-Four"
book.save()

book = Book.objects.get(author="George Orwell")
book.title
# Output: 'Nineteen Eighty-Four'
