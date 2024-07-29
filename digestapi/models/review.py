from django.db import models
from .book import Book
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.CharField(max_length=511)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""Review of {self.book.title} by {self.user.first_name} {self.user.last_name} on {self.date_created}
{self.rating} Stars
{self.content}
"""