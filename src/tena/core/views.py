from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixins, PermissionRequiredMixin

class LPRequiredMixin(LoginRequiredMixins, PermissionRequiredMixin):
	""" Used to include both LoginRequiredMixin and PermissionRequiredMixin
		together. """
	pass

# Branch CRUD Views

class AddBranchView(LPRequiredMixin, CreateView):
	pass

class UpdateBranchView(LPRequiredMixin, CreateView):
	pass

class ListBranchView(LPRequiredMixin, ListView):
	pass

class RemoveBranchView(LPRequiredMixin, ListView):
	pass


# Bus CRUD Views
class AddBusView(LPRequiredMixin, CreateView):
	pass

class UpdateBusView(LPRequiredMixin, CreateView):
	pass

class ListBusView(LPRequiredMixin, ListView):
	pass

class RemoveBusView(LPRequiredMixin, ListView):
	pass


# Driver CRUD Views
class AddDriverView(LPRequiredMixin, CreateView):
	pass

class UpdateDriverView(LPRequiredMixin, CreateView):
	pass

class ListDriverView(LPRequiredMixin, ListView):
	pass

class RemoveDriverView(LPRequiredMixin, ListView):
	pass


# Route CRUD Views
class AddRouteView(LPRequiredMixin, CreateView):
	pass

class UpdateRouteView(LPRequiredMixin, CreateView):
	pass

class ListRouteView(LPRequiredMixin, ListView):
	pass

class RemoveRouteView(LPRequiredMixin, ListView):
	pass


# Ticket CRUD Views
class AddTicketView(LPRequiredMixin, CreateView):
	pass

class UpdateTicketView(LPRequiredMixin, CreateView):
	pass

class ListTicketView(LPRequiredMixin, ListView):
	pass

class RemoveTicketView(LPRequiredMixin, ListView):
	pass


# Receipt CRUD Views
class AddReceiptView(LPRequiredMixin, CreateView):
	pass

class UpdateReceiptView(LPRequiredMixin, CreateView):
	pass

class ListReceiptView(LPRequiredMixin, ListView):
	pass

class RemoveReceiptView(LPRequiredMixin, ListView):
	pass


# Appointement CRUD Views
class AddAppointementView(LPRequiredMixin, CreateView):
	pass

class UpdateAppointementView(LPRequiredMixin, CreateView):
	pass

class ListAppointementView(LPRequiredMixin, ListView):
	pass

class RemoveAppointementView(LPRequiredMixin, ListView):
	pass





