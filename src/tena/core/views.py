from django.views.generic import CreateView, UpdateView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from core.forms import SearchRouteForm

class LPRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
	""" Used to include both LoginRequiredMixin and PermissionRequiredMixin
		together. """
	pass


class SearchRouteView(FormView):
	form_class = SearchRouteForm
	template_name = "core/search_route.html"
