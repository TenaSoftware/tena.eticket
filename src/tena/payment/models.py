from django.db import models
from ausers.models import Customer
from core.models import Route

class CheckOut(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)
	date_paid = models.DateTimeField(auto_now_add=True)
