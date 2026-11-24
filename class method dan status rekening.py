class BankAccount:
    no = 0
    balance = 0
    active = True

    def __init__(self, no, balance=0):
        if balance < 0:
            raise ValueError("Gagal! Saldo tak boleh minus.")

        self.no = no
        self.balance = balance

    @classmethod
    def disabled(cls, no, balance=0):
        result = cls(no, balance)
        result.active = False
        return result


Bank_Account1 = BankAccount("1", 10000)
Bank_Account2 = BankAccount.disabled("2", -200000)

try:
    Bank_Account2 = BankAccount.disabled("2", -200000)
except ValueError as e:
    print(e)

print(f"Bank Account {Bank_Account1.no} has balance {Bank_Account1.balance} and status {Bank_Account1.active}")
print(f"Bank Account {Bank_Account2.no} has balance {Bank_Account2.balance} and status {Bank_Account2.active}")
