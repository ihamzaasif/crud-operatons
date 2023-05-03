from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('first', type=int, help='A number less then 100')
        parser.add_argument('--option1', default='default', help='The option1 Value')

    def handle(self, *args, **options):
        # print('Command: mycommand')
        # print('Second Line')
        # print(f'First: {options["first"]}')
        # print(f'Option1: {options["option1"]}')
        if options['first'] < 100:
            self.stdout.write(self.style.SUCCESS('The number is less than 100'))
        else:
            raise CommandError ('The number is greater then 100')
        
        self.stdout.write(f'The Value of --option1 is {options["option1"]}')