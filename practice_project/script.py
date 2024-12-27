import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice_project.settings')  # Замените myproject на имя вашего проекта
django.setup()

from practice_app.models import *

# Task 1
p1 = Product.objects.create(name="iphone", price=2000.0, discount=15.0)
final_price = p1.final_price
print("Task 1")
print("Исходная цена:", p1.price)
print(f"Цена продукта с учетом скидки {p1.discount}%:", final_price)
p1.apply_discount(20)

#Task 2
a1 = Author.objects.create(name="Andrew", birth_date=date(1999, 5, 12))
print("\nTask 2")
print("Возраст:", a1.age)
b1 = Book.objects.create(title="title1", author=a1, pages=110)
print(b1.short_description())