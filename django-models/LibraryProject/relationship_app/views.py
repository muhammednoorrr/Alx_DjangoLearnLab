from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


# --- Book permission-protected views ---

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return HttpResponse("You have permission to add a book.")

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    return HttpResponse(f"You have permission to edit book with id {book_id}.")

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    return HttpResponse(f"You have permission to delete book with id {book_id}.")
# Helpers to check roles
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# Registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # <- use UserCreationForm() here
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()  # <- use UserCreationForm() here
    return render(request, "relationship_app/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Change "home" to the desired page
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
# Function-based view: list all books
def list_books_view(request):
    books = Book.objects.all()  # Must be explicitly included
    return render(request, "relationship_app/list_books.html", {"books": books})  # Must reference template

# Class-based view: display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Must reference template
    context_object_name = "library"  # Must be 'library' for template access
