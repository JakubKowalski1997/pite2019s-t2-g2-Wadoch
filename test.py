import unittest
from Bank import Bank
from Client import Client

class Test(unittest.TestCase):
    def test_add_clientss(self):
        bank = Bank("TEST")
        client = Client("TEST")
        bank.add_client(client)
        self.assertEqual(client, bank.clients[0])

    def test_withdraw(self):
        bank = Bank("TEST")
        client = Client("TEST")
        bank.add_client(client)
        bank.withdraw(client, 100)
        self.assertEqual(-100, client.money)

    def test_deposit(self):
        bank = Bank("TEST")
        client = Client("TEST")
        bank.add_client(client)
        bank.deposit(client, 100)
        self.assertEqual(100, client.money)

    def test_send_money_between_clients(self):
        bank = Bank("TEST")
        client1 = Client("TEST")
        client2 = Client("TEST2")
        bank.add_client(client1)
        bank.add_client(client2)
        bank.deposit(client1, 100)
        bank.send_money_between_clients(client1,client2, 100)
        self.assertEqual(100, client2.money)
    
    def test_withdraw_money(self):
        client = Client("TEST")
        client.withdraw_money(100)
        self.assertEqual(-100, client.money)

    def test_deposit_money(self):
        client = Client("TEST")
        client.deposit_money(100)
        self.assertEqual(100, client.money)

    def test_init_client(self):
        client = Client("TEST")
        self.assertEqual("TEST", client.name)

    def test_init_bank(self):
        bank = Bank("TEST")
        self.assertEqual("TEST", bank.name)

    def test_init_bank_got_own_money(self):
        bank = Bank("TEST")
        self.assertEqual(10000, bank.stored_money)

    def test_deposit_increase_stored_money(self):
        bank = Bank("TEST")
        client = Client("TEST")
        bank.add_client(client)
        bank.deposit(client, 100)
        self.assertEqual(10100, bank.stored_money)

    def test_withdraw_decrease_stored_money(self):
        bank = Bank("TEST")
        client = Client("TEST")
        bank.add_client(client)
        bank.withdraw(client, 100)
        self.assertEqual(9900, bank.stored_money)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")