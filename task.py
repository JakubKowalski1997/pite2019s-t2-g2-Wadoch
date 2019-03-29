from Bank import Bank
from Client import Client

if __name__ == "__main__":	
	bank = Bank('bank')
	
	bank.add_client(Client('First'))
	bank.add_client(Client('Second'))
	bank.add_client(Client('Third'))
	
	bank.log()
	bank.send_money_between_clients(bank.clients[1], bank.clients[2], 100)
	bank.log()
	bank.withdraw(bank.clients[0], 100)
	bank.log()

