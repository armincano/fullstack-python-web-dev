from django.shortcuts import render

def home(request):
    return render(request, "palindrome/home.html")

def is_palindrome(request, word):
    is_palindrome = word.lower().replace(" ", "") == word[::-1].lower().replace(" ", "")
    context = {"word": word, "is_palindrome": is_palindrome}
    return render(request, "palindrome/is_palindrome.html", context)