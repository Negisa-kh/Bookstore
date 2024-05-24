from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def search(req):
    return render(req, "books/search.html")

def book_detail(req):
    return render(req, "books/book_detail.html")