from django.core.management.base import BaseCommand, CommandError
from practice_app.models import Product

class Command(BaseCommand):
    help = 'Обнуляет кол-во всех товаров'

    def handle(self, *args, **options):
        for product in Product.objects.all():
            product.quantity = 0
            product.save()

            self.stdout.write(self.style.SUCCESS('Successfully nulled product "%s"' % str(product)))
