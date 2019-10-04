import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
# Import settings
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for i in range(N):
        fake_fName = fakegen.first_name()
        fake_lName = fakegen.last_name()
        fake_email = fakegen.free_email()
        user = User.objects.get_or_create(fName=fake_fName,lName=fake_lName,email=fake_email)[0]
        user.save()

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
