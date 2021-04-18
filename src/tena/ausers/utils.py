"""
`ausers` utilities for tena project.

Generated Manually from Linux terminal
 * NAME: Wendirad Demelash
 * DATE: April 3, 2021
"""
import re

from decouple import config
from twilio.rest import Client


class TwilioMessage:
    """
    A class to organize twilio messaging API.

    ...

    Attributes
    ----------
    ACCOUNT_SID: str
        account sid generated from twilio manually.
    ACCOUNT_TOKEN: str
        token to verify account
    SERVICE_ID: str
        id to verify service in twilio.
    MSG_SERVICE: str
        id to get messaging service from twilio.
    INTERNATIONAL: regex
        regex to identify phone number format
    """

    ACCOUNT_SID = config("ACCOUNT_SID_TRIAL", cast=str)
    AUTH_TOKEN = config("AUTH_TOKEN_TRIAL", cast=str)
    SERVICE_ID = config("SERVICE_ID_TRIAL", cast=str)
    MSG_SERVICE = config("MSG_SERVICE", cast=str)
    INTERNATIONAL = r"\+2519\d{8}$"  # E.16 format phone number

    def __init__(self):
        """ Initialize verifer using client """
        self.client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

    def formated_number(self, number):
        """convert number to E.16 format
        It need to be changed b/c twilio require
        E.16 format number."""
        if re.match(self.INTERNATIONAL, number):
            return number
        return f'+251{number.lstrip("0")}'

    def send_verification(self, number):
        """ Send 5 digit verification code to user when required."""
        verification = self.client.verify.services(
            self.SERVICE_ID
        ).verifications.create(to=self.formated_number(number), channel="sms")
        return verification.status

    def verify_code(self, number, code):
        """ verify users verification code based on their number """
        verification_check = self.client.verify.services(
            self.SERVICE_ID
        ).verification_checks.create(to=self.formated_number(number), code=code)
        return verification_check.status

    def send_message(self, number, body):
        """ send message to a given number using registered messaging service """
        self.client.messages.create(
            body=body,
            messaging_service_sid=self.MSG_SERVICE,
            to=self.formated_number(number),
        )


twilio_message = TwilioMessage()
