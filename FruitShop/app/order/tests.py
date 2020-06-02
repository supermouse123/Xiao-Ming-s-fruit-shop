from django.test import TestCase
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fruitshop.settings")
# django.setup()
from django.contrib.auth.hashers import make_password,check_password
# Create your tests here.

a = make_password('123456789')
b = check_password('123456789', 'pbkdf2_sha256$36000$nQKUQg4yBgdx$m5NXc1MYGwYQv/qARMuc1vfeherIcYg7HaGIGG1Af9M=')
print(a)
print(b)