from abc import ABCMeta, abstractmethod


class Vehicle(object):
	"""A vehicle for sale by dealership:
	
	Attributes:
		wheels: An integer representing the number of wheels the vehicle has
		miles: the itegral number of miles driven on the vehicle
		make: the make of the vehicle as a string.
		model: the model of the vehicle as a string.
		year: the integral year the vehicle was built.
		sold_on: the date the vehicle was sold
	"""

	__metaclass__ = ABCMeta
	 
	base_sale_price = 0
	wheels = 0
	
	def __init__(self, wheels, miles, make, model, year, sold_on):
		"""Return a new Vehicle object."""
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on
		
	def sale_price(self):
		"""Return the sale price for this vehicle as a float amount."""
		if self.sold_on is not None:
			return 0.0 # Already sold
		return 5000.0 * self.wheels
		
	def purchase_price(self):
		"""Return the price for which we would pay to purchase the vehicle."""
		if self.sold_on is None:
			return 0.0 # Not yet sold
		return self.base_sale_price - (.10 * self.miles)
		
	@abstractmethod
	def vehicle_type(self):
		"""Return a string representing the type of vehicle this is."""
		pass
		

class Car(Vehicle):
	""" A car for sale by car Dealearship."""
	
	base_sale_price = 8000
	wheels = 4
	
	def vehicle_type(self):
		"""Return a string representing the type of vehicle this is."""
		return 'car'
		

class Truck(Vehicle):
	""" A truck for sale by ar Dealership."""
	
	base_sale_price = 10000
	wheels = 4
	
	def vehicle_type(self):
		"""Return a string representing the type of vehicle this is."""
		return 'truck'
		
		
		
class Motorcycle(Vehicle):
	"""A motorcycle for sale by Car Dealership."""
	
	base_sale_price = 4000
	wheels = 2
	
	def vehicle_type(self):
		"""Return a string representing the type of vehicle this is."""
		return 'motorcycle'
		

car1 = Car(4, 3000, "toyota", "camry", "2015", "2015")
print car1.vehicle_type()
print car1.purchase_price()
print car1.sale_price()
	