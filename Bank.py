class Bank:
	def __init__(self, name):
		self.name = name
		self.clients = []
		self.stored_money = 10000
		pass

	def log(self):
		print("BANK: {} - {} PLN".format(self.name, self.stored_money))
		self.log_clients()
		print("\n")

	def log_clients(self):
		for client in self.clients:
			client.log()

	def add_client(self, client):
		self.clients.append(client)

	def send_money_between_clients(self, client1, client2, value):
		client1.withdraw_money(value)
		client2.deposit_money(value)

	def withdraw(self, client, value):
		client.withdraw_money(value)
		self.stored_money -= value

	def deposit(self, client, value):
		client.deposit_money(value)
		self.stored_money += value
		
