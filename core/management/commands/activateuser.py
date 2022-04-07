from argparse import ArgumentParser

from django.core.management import BaseCommand, CommandError

from core.models import User


class Command(BaseCommand):
    help = 'A django command for active a user!'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-p', '--phone', help='Enter your phone!')

    def handle(self, *args, **options):
        phone = options['phone']
        if User.objects.get(username=phone):
            raise CommandError("This phone is not exist!")
        else:
            self.p = User.objects.get(username=phone)
            self.p.is_active = True
