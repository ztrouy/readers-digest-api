from django.db import models
from .book import Book
from .category import Category


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.category.name}"