from django.db import models
from ausers.models import Customer

class Company(models.Model):
	name = models.CharField(max_length=150)

class Branch(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	name  = models.CharField(max_length=150)


class Driver(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	licence_level = models.CharField(max_length=150)

class Bus(models.Model):
	LEVEL = (
		('1', 'Level One'),
		('2', 'Level Two'),
		('3', 'Level There')
	)
	driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
	plate_number = models.PositiveIntegerField()
	side_number = models.PositiveIntegerField()
	level = models.CharField(max_length=2, choices=LEVEL)

class Route(models.Model):
	bus = models.ManyToManyField(Bus)	
	start_station = models.CharField(max_length=150)
	destination = models.CharField(max_length=150)
	is_active = models.BooleanField(default=True)
	date_create = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
	route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	date_issued = models.DateTimeField(auto_now_add=True)
	seat_number = models.PositiveIntegerField()

class Receipt(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	date_issued = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
	description = models.CharField(max_length=500)
	date_issued = models.DateTimeField(auto_now_add=True)

class Appointement(models.Model):
	start_station = models.CharField(max_length=150)
	destination = models.CharField(max_length=150)
	date_appointed = models.DateTimeField(auto_now_add=True)
	date_to_appoint = models.DateTimeField(auto_now_add=True)
