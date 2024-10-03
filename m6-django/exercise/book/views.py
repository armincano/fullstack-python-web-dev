from django.shortcuts import render

def home(request):
    return render(request, "book/home.html")

def book_list(request):
    context = {
        "books": [
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 10.99},
            {"title": "1984", "author": "George Orwell", "price": 8.99},
            {"title": "Moby Dick", "author": "Herman Melville", "price": 12.50},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 9.99},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 14.00},
            {"title": "War and Peace", "author": "Leo Tolstoy", "price": 19.99},
            {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 7.99},
        ]
    }
    return render(request, "book/book_list.html", context)