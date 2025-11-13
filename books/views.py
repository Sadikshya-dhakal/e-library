from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Q

# Create your views here.


def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'books/add_book.html')

def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('book_list')
    return render(request, 'books/update_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')


def mark_as_read(request, id):
    book = get_object_or_404(Book, id=id)
    book.is_read = True
    book.save()
    return redirect('book_list')


