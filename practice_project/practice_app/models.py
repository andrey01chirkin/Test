from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


# Товар для нашей витрины
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    # допишем свойство, которое будет отображать, есть ли товар на складе
    @property
    def on_stock(self):
        return self.quantity > 0

    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
