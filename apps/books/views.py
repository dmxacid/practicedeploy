from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Author, Book, Publisher

# Create your views here.
def index(request):
	context = {
		"authors": Author.objects.all(),
		"books": Book.objects.all(),
		"publishers": Publisher.objects.all(),
	}

	return render(request, "books/index.html", context)

def create_author(request):
	res = Author.objects.add_author(request.POST)

	if res["added"]:
		messages.success(request, "Added author {}".format(res["new_author"].name))
	else:
		for error in res["errors"]:
			messages.error(request, error)

	return redirect("index")

def create_book(request):
	author = Author.objects.get(id=request.POST["author"])
	Book.objects.create(title=request.POST["title"], rating=request.POST["rating"], author=author)
	return redirect("index")

def create_publisher(request):
	Publisher.objects.create(name=request.POST["name"])
	return redirect("index")

def add_book_to_publisher(request):
	print(request.POST)
	book = Book.objects.get(id=request.POST["book_id"])
	publisher = Publisher.objects.get(id=request.POST["publisher_id"])
	publisher.books.add(book)
	return redirect("index")
