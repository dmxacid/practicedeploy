from django.db import models

class AuthorManager(models.Manager):
	def add_author(self, data):
		errors = []

		if not data["name"]:
			errors.append("Enter a name")
		elif len(data["name"]) < 2:
			errors.append("Name must be at least 2 characters long")

		response = {}

		if not errors:
			new_author = self.create(name=data["name"])
			response["added"] = True
			response["new_author"] = new_author
		else:
			response["added"] = False
			response["errors"] = errors

		return response

class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = AuthorManager()

class Book(models.Model):
	title = models.CharField(max_length=255)
	rating = models.IntegerField()
	author = models.ForeignKey(Author, related_name="books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
