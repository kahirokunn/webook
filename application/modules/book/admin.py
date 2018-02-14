from django.contrib import admin
from modules.book.models import Book
from modules.book.models import Category

admin.site.register(Book)
admin.site.register(Category)
