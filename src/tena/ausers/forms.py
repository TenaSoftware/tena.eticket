"""
`ausers` forms for tena project.

Generated by 'python3 manage.py startapp' using Django 3.1.7.
 * NAME: Wendirad Demelash
 * DATE: April 3, 2021
"""
from django.contrib.auth.forms import UserCreationForm

from ausers.models import Customer

class SignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('phone_number',)