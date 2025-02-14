from django.db import models

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.code

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Bookshelf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1024)  #  Match database type
    languages = models.ManyToManyField("Language", related_name="books")
    subjects = models.ManyToManyField("Subject", related_name="books")
    bookshelves = models.ManyToManyField("Bookshelf", related_name="books")
    media_type = models.CharField(max_length=16)  #  Match database field
    download_count = models.IntegerField(null=True, blank=True)  #  Match database field
    gutenberg_id = models.IntegerField(unique=True)  #  Match database field
    authors = models.ManyToManyField("Author", through="BookAuthors")

    def __str__(self):
        return self.title


class BookAuthors(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_id')

    class Meta:
        db_table = "books_book_authors"
