import os

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_ajax_search_project.settings')

import django

# Import settings
django.setup()

import random
from django.contrib.auth.models import User
from faker import Faker

fakegen = Faker()
global user_name_list
user_name_list = []


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        if fake_first_name not in user_name_list:
            user_name_list.append(fake_first_name)
            fake_last_name = fake_name[1]
            fake_email = fakegen.email()
            password = fake_first_name + fake_last_name + 'pass99'

            # Create new User Entry
            user = User.objects.get_or_create(username=fake_first_name,
                                            first_name=fake_first_name,
                                            last_name=fake_last_name,
                                            email=fake_email,
                                            password=password)[0]
            user.set_password(user.password)
            user.save()
            print(entry)


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
