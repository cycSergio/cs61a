# Q1: Next Fibonacci Object
class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        # "*** YOUR CODE HERE ***"
        class MyFib():

            def __init__(self, value=0):
                self.value = value
                self.previous = 1

            def next(self):
                old_value = self.value
                self.value = self.value + self.previous
                self.previous = old_value
                #print(self.value, self.previous, old_value)
                return self

            def __repr__(self):
                return str(self.value)
        a = MyFib()
        return a.next()

    def __repr__(self):
        return str(self.value)


# Q2： a VendingMachine
class VendingMachine:
    """A vending machine that vends some product for some price.
    当没有存货的时候，deposit会被拒绝

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.balance = 0
        self.quantity = 0

    def restock(self, amount):
        self.quantity += amount
        return 'Current {0} stock: {1}'.format(self.product, self.quantity)

    def vend(self):
        if self.quantity == 0:
            return 'Machine is out of stock.'
        elif self.quantity > 0 and self.balance == self.price:
            self.balance = 0
            self.quantity -= 1
            return 'Here is your {0}.'.format(self.product)
        elif self.quantity > 0 and self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0
            self.quantity -= 1
            return 'Here is your {0} and ${1} change.'.format(self.product, change)
        elif self.quantity > 0 and self.balance < self.price:
            diff = self.price - self.balance
            return 'You must deposit ${0} more.'.format(diff)

    def deposit(self, amount):
        if self.quantity == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)
        else:
            self.balance += amount
            return 'Current balance: ${0}'.format(self.balance)
