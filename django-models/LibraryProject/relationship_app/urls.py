from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
from .views import (
    list_books_view,
    LibraryDetailView,
    register_view,

)


urlpatterns = [
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    
    # Function-based registration view
    path("register/", views.register_view, name="register"),
    
    # Other existing views
    path("books/", views.list_books_view, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
