"""
    YenePay RESTAPI module in python3

    NAME: Wendirad Demelash
    DATE: May 7, 2021
"""

from collections import namedtuple

import requests
from django.conf import settings


class YenePay:
    """ YenePay RESTAPI implementation. """

    checkout_url = namedtuple('checkout', ('production', 'sandbox'))
    pdt_url = namedtuple('pdt', ('production', 'sandbox'))
    ipn_url = namedtuple('checkout', ('production', 'sandbox'))

    def __init__(self, is_sandbox=False):
        """ Initialization of YenePay RESTAPI. """
        self.is_sandbox = is_sandbox
        self.header = {'Content-Type': 'application/json'}

        self.checkout_url.production = 'https://endpoints.yenepay.com/api/urlgenerate/getcheckouturl/'
        self.checkout_url.sandbox = 'https://testapi.yenepay.com/api/urlgenerate/getcheckouturl/'

        self.pdt_url.production = 'https://testapi.yenepay.com/api/urlgenerate/getcheckouturl/'
        self.pdt_url.sandbox = 'https://testapi.yenepay.com/api/verify/pdt/'

        self.ipn_url.production = 'https://endpoints.yenepay.com/api/verify/ipn'
        self.ipn_url.sandbox = 'https://testapi.yenepay.com/api/verify/ipn/'


    def checkout(self, **kwargs):

        """
            Creates a new payment order on YenePay for
            the authenticated user and redirects to checkout
            application to complete the payment.
        """
        url = getattr(self.checkout_url, 'sandbox' if self.is_sandbox else 'production')
        res = requests.post(url, json=kwargs, headers=self.header)
        return res

    def pdt(self, **kwargs):

        """ Checks the latest status of a payment order. """
        url = getattr(self.pdt_url, 'sandbox' if self.is_sandbox else 'production')
        res = requests.post(url, json=kwargs, headers=self.header)
        return res.json()


    def ipn(self, **kwargs):
        """ Verifies the validity and integrity of a received IPN request on your IPN endpoint. """
        url = getattr(self.ipn_url, 'sandbox' if self.is_sandbox else 'production')
        res = requests.post(url, json=kwargs, headers=self.header)
        return res



yenepay = YenePay(is_sandbox=settings.YENEPAY.get('SANDBOX', None))
