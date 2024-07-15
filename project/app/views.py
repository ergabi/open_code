from django.shortcuts import render,redirect
from .models import Book
from django.db.models import Q
from .forms import BookForm ,BookSearchForm

def book_list(request):
    books = Book.objects.all()
    return render(request,'index.html',{'books':books})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'book.html',{'form':form})
    
def book_update(request,id):
    book = Book.objects.filter(id=id).first()
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book.html', {'form': form})
    
def book_delete(request,id):
    book = Book.objects.filter(id = id).first()
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request,'book.html',{'book':book})

def book_search(request):
    form = BookSearchForm(request.GET)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            books = books.filter(Q(title__icontains=query) |Q(author__icontains=query))

    return render(request, 'search.html', {'books': books, 'form': form})