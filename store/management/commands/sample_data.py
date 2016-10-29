from django.core.management.base import BaseCommand, CommandError
from store.models import Product
import random
import string

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('product_count', nargs='+', type=int)

    def handle(self, *args, **options):
        def random_name():
            return "product_%s" % (''.join([ random.choice(string.letters) for i in range(10)] ))
        def random_price():
            return random.randint(100, 300)

        def random_score():
            return random.randint(0, 10)
        def random_amount():
            return random.randint(0, 100)

        for product_count in options['product_count']:
            for i in range(product_count):
                product = Product(name=random_name(), price=random_price(), amount=random_amount(), score=random_score())
                product.save()
