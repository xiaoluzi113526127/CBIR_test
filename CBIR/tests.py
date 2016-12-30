from django.test import TestCase

# Create your tests here.


def a():
    b=3
    d = 5
    return b,d
m,_=a()
print m