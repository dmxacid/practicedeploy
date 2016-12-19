from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^create_book/", views.create_book, name="create_book"),
	url(r"^create_author/", views.create_author, name="create_author"),
	url(r"^create_publisher/", views.create_publisher, name="create_publisher"),
	url(r"^add_book_to_publisher", views.add_book_to_publisher, name="add_book_to_publisher"),
]
