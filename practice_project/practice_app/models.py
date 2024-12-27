from datetime import date
from django.db import models

# Task 1
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)
    created_at = models.DateField(auto_now_add=True, null=True)

    @property
    def final_price(self):
        return self.price * (100 - self.discount)/100

    def apply_discount(self, amount):
        self.discount = amount
        self.save()


#Task 2
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year

        # Учитываем, наступил ли день рождения в текущем году
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1

        return age

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    pages = models.IntegerField()

    def short_description(self):
        return f"Название книги: {self.title}, автор: {self.author.name}"

