from django.core.management.base import BaseCommand
from academics.models import User
import json

class Command(BaseCommand):
    #Configure help information
    help = 'Make a database backup in JSON format'
    
    def handle(self, *args, **options) -> str | None:
        #Get data from User model
        users = User.objects.all()

        #convert data to dictionaries
        data = [ 
            {
            'email':user.email,
            'password':user.password,
            'status':user.status
            }
            for user in users
        ]

        #Save to JSON format
        with open('backup_db.json','w') as file:
            json.dump(data,file,indent=4)