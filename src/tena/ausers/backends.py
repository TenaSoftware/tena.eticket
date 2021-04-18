"""
`ausers` backends for tena project.

Generated Manually from Linux terminal
 * NAME: Wendirad Demelash
 * DATE: April 3, 2021
"""
import re

from django.contrib.auth.backends import ModelBackend

from ausers.models import Customer
from ausers.utils import twilio_message


class CustomerBackend(ModelBackend):
    """Customer Backend to enable customers authenticate
    both with 10 and 13 digit number"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(Customer.USERNAME_FIELD)
        if username is None or password is None:
            return None
        if re.match(r"^09\d{8}$", username):
            username = twilio_message.formated_number(username)
        return super().authenticate(request, username, password, **kwargs)
