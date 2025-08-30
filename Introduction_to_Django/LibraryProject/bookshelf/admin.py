from django.contrib import admin
from .models import Book

# Customize the Book admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    search_fields = ('title', 'author')  # Enable search by title or author
    list_filter = ('publication_year',)  # Filter by publication year

# Register Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)
