from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.sites.shortcuts import get_current_site


class SiteRequiredMixin(UserPassesTestMixin):
    site_id = None
    permission_denied_message = "Sorry, you'r request can't be processed."

    def verfiy_site(self):
        if self.site_id is None:
            raise ImproperlyConfigured("You must give site_id to class attribute.")
        return get_current_site(self.request).id == self.site_id

    def get_test_func(self):
        return self.verfiy_site
