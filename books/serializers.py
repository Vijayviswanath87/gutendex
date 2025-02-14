from rest_framework import serializers
from .models import Book, Author, Subject, Bookshelf, Language

class LanguageSerializer(serializers.ModelSerializer):
    """
    Serializer for Language model.
    """
    class Meta:
        model = Language
        fields = ['code']


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Subject model.
    """
    class Meta:
        model = Subject
        fields = ['name']


class BookshelfSerializer(serializers.ModelSerializer):
    """
    Serializer for Bookshelf model.
    """
    class Meta:
        model = Bookshelf
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    """
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    Includes related fields: authors, subjects, bookshelves, languages.
    """
    subjects = SubjectSerializer(many=True)
    bookshelves = BookshelfSerializer(many=True)
    languages = LanguageSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'languages', 'subjects', 'bookshelves', 'media_type', 'download_count', 'gutenberg_id']
