from django.core.management.base import BaseCommand, CommandError
from PIL import Image
import os

class Command(BaseCommand):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"

    def add_arguments(self, parse):
        parse.add_argument('width', nargs="+", type=int)
        parse.add_argument('height', nargs="+", type=int)

    def handle(self, *args, **options):
        my_path = self.ROOT_DIR + "../../../static/product_image/"
        onlyfiles = [f for f in os.listdir(my_path) if any(word in f for word in ["png", "jpg"])]
        newsize = options['width'][0], options['height'][0]
        for filename in onlyfiles:
            filename = my_path + filename
            img = Image.open(filename)
            img = img.resize((newsize), Image.ANTIALIAS)
            img.save(filename)

