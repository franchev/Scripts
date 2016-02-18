class Employee(object):
	""" Employees at frany kool
	
	attributes:
		firstname: first name of employee
		lastname: lastname of employee
		hire_date: date employee was hired
		department: department employee belong to
		employment_type: full-time salary or contract
	"""
	
	base_salary_per_day = 300
	
	def __init__(self, firstname, lastname, hire_date='02/17/2016', department='all', employment_type):
		"""Return attributes for employee"""
		
		self.firstname = firstname
		self.lastname = lastname
		self.hire_date = hire_date
		self.department = department
		self.employment_type = employment_type
		
	def employee_report(self):
		"""Print information about employee"""
		
		print "firstname = %s" % self.firstname
		print "lastname = %s" % self.lastname
		print "hire Date = %s" % self.hire_date
		print "department = %s" % self.department
		print "employment type = %s" % self.employment_type
	
	def pay_report(self):
		"""Print information about payment to employee, default to full-time salary"""
		
		pay = self.base_salary_per_day * 15
		print "firstname: %s lastname: %s\n department: %s employment type: %s\n netpay: %d" %(self.firstname, self.lastname, self.department,
		                                                                                                                                                        self.employment_type, pay)
		
class Salary_based(Employee):
	""" Return salary based paycheck"""

	pass
	
	
class contract_based(Employee):
	""" Return contract based employee"""
	
	base_salary_per_hour = 15
	def pay_report(self):
		"""Print information about payment to employee, default to full-time salary"""
		
		pay = (self.base_salary_per_hour *  40) * 2
		print "firstname: %s lastname: %s\n department: %s employment type: %s\n netpay: %d" %(self.firstname, self.lastname, self.department,
		                                                                                                                                                        self.employment_type, pay)
	
	
	
	