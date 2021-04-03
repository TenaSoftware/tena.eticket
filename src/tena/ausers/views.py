"""
`ausers` views for tena project.

Generated by 'python3 manage.py startapp' using Django 3.1.7.
 * NAME: Wendirad Demelash
 * DATE: April 3, 2021
"""

from django.contrib.auth import get_user_model
from django.views.generic import CreateView

from ausers.forms import SignUpForm
from ausers.models import Customer

class SignUpView(CreateView):
    model = Custom
    form_class = SignUpForm
    template_name = 'ausers/signup_form.html'
