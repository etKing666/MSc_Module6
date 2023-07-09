# INSTRUCTIONS: Amend the code so that the tests fail.

# A clumsy programmer mixes up the += with -= and > with < so he makes some mistakes. And he also finds out that he
# added "5" to the initial amount supposedly because his cat walked on his keyboard!

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount + 5

    def spend_cash(self, amount):
        if self.balance > amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance += amount

    def add_cash(self, amount):
        self.balance -= amount