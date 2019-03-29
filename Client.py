class Client:
	def __init__(self, name):
		self.money = 0
		self.name = name

	def log(self):
		print("{}: {} PLN".format(self.name, self.money))

	def withdraw_money(self, value):
		self.money -= value

	def deposit_money(self, value):
		self.money += value