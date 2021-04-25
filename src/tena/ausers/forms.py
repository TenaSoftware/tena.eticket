"""
`ausers` forms for tena project.

Generated Manually from Linux terminal
 * NAME: Wendirad Demelash
 * DATE: April 3, 2021
"""
import logging

from django import forms
from django.contrib.auth.forms import PasswordResetForm as AuthPasswordRestForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from twilio.base.exceptions import TwilioRestException

from ausers.models import Customer
from ausers.utils import twilio_message


class SignUpForm(UserCreationForm):
    """ SignUp form check validation and send verification code to customer. """

    class Meta:
        model = Customer
        fields = (
            "phone_number",
            "first_name",
            "last_name",
            "sex",
            "date_of_birth",
            "region",
            "zone",
            "woreda",
            "house_number",
        )

    def clean_phone_number(self):
        """ check and return E.16 form phone_number. """
        super().clean()
        phone_number = self.cleaned_data.get("phone_number", None)
        return twilio_message.formated_number(phone_number)


class VerficationForm(forms.Form):
    """ A form to check user enters valid verification code. """

    code = forms.RegexField(
        r"^\d{5}$",
        widget=forms.TextInput(
            attrs={"pattern": "[0-9]{5}", "title": "5 digit verification code"}
        ),
        help_text="Enter 5 digit verification code sent to your " "phone number.",
    )

    def __init__(self, request, *args, **kwargs):
        """ initialize a form with request attribute. """
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_code(self):
        """send verification to code to users and save in session
        for further verification."""
        code = self.cleaned_data.get("code", None)
        if code is None:
            raise forms.ValidationError(
                _(
                    "Please, enter the valid verification code sent "
                    "to your phone number. "
                ),
                code="invalid",
            )
        phone_number = self.request.session.get("phone_number")
        try:
            verification_status = twilio_message.verify_code(phone_number, code)
        except TwilioRestException as error:
            logging.error(error)
            raise forms.ValidationError(_("Something went wrong. Please try again!"))
        if verification_status != "approved":
            raise forms.ValidationError(
                _(
                    "Please, enter the valid verification code sent "
                    "to your phone number. "
                ),
                code="invalid",
            )
        return code


class PasswordResetForm(AuthPasswordRestForm):
    """ Extend default PasswordResetForm to accept both email and phone number."""

    email = forms.RegexField(
        r"((\+2519|09)\d{8}$)|(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        label=_("Phone number/ Email"),
    )
