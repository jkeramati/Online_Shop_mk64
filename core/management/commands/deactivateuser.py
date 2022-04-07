from argparse import ArgumentParser

from django.core.management import BaseCommand, CommandError

from core.models import User


class Command(BaseCommand):
    help = 'A django command for deactive a user!'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-p', '--phone', help='Enter your phone!')

    def handle(self, *args, **options):
        phone = options['phone']
        p = User(phone=phone)
        if not User.objects.filter(phone=phone) and p.is_active == True:
            raise CommandError("This phone is not exist!")
        else:
            p.is_active = False
