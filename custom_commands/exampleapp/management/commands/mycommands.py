from typing import Any
from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):

    help = 'The help info for this command is: '


    def add_arguments(self,parser):
        parser.add_argument('first', type=int,help='Number less than 100' )
        parser.add_argument('second',nargs=3,type=str,help='Three strings')
        parser.add_argument('--option1',default='default',help='option1 value')
        parser.add_argument('--option2',action='store_true',help='True if passed')

    def handle(self, *args, **options):
        # print("Command: myCommand")
        # print('Second Line')

        # print(f'First: {options["first"]}')
        # print(f'option1 {options["option1"]}')


        if options['first'] < 100:
            self.stdout.write(self.style.SUCCESS('Good job the number is less than 100'))

        else:
             raise CommandError('That number is greater than 100')
        
        for value in options['second']:
            self.stdout.write(self.style.SUCCESS(f'Value: {value}'))
        
        self.stdout.write(f'the value of --option1 is : {options["option1"]}')

        if options['option2']:
            self.stdout.write(self.style.SUCCESS('option2 is TRUE'))

        else:
            self.stdout.write(self.style.WARNING('option2 is FALSE'))
