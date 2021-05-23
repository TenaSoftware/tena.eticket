from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic import CreateView, FormView, ListView, UpdateView

from core.forms import SearchRouteForm


class LPRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
	""" Used to include both LoginRequiredMixin and PermissionRequiredMixin
		together. """
	pass

class SearchRouteView(LPRequiredMixin, FormView):
    form_class = SearchRouteForm
    template_name = "core/search_route.html"
    permission_required = ()
    
    def form_valid(self, form):
        print(form.data)
