"""
`ausers` forms for tena project.

Generated Manually from Linux terminal
 * NAME: Wendirad Demelash
 * DATE: April 3, 2021
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from twilio.base.exceptions import TwilioRestException
from ausers.models import Customer
from ausers.utils import twilio_verify

class SignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ( 'first_name', 'last_name', 'sex',
        'region', 'zone', 'woreda', 'house_number', 'phone_number',)

    def clean_phone_number(self):
        super().clean()
        phone_number = self.cleaned_data.get('phone_number', None)
        return twilio_verify._formated_number(phone_number)

class VerficationForm(forms.Form):
    code = forms.RegexField(
        r'^\d{5}$',
        widget=forms.TextInput(
            attrs = {
                "pattern": "[0-9]{5}",
                "title": "5 digit verification code"
            }
        ),
        help_text='Enter 5 digit verification code sent to your '
                   'phone number.'
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_code(self):
        code = self.cleaned_data.get('code', None)
        if code is None:
            raise forms.ValidationError(_('Please, enter the valid verification code sent '
                        'to your phone number. '), code='invalid')
        phone_number = self.request.session.get('phone_number')
        try:
            verification_status = twilio_verify.verify_code(phone_number, code)
        except TwilioRestException as e:
            raise forms.ValidationError(_("Something went wrong. Please try again!"))
        if verification_status != 'approved':
            raise forms.ValidationError(_('Please, enter the valid verification code sent '
                        'to your phone number. '), code='invalid')
        return code
