from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    """An extension to BankAccount that issue interest."""
    
    def __init__(self, customer, bank, balance, interest_rate):
        """Create a chequing account instance.
        customer               the name of the customer
        bank                   the name of the bank
        balance                the account balance
        interest_rate          the interest rate for paying interest
        """
        
        super().__init__(customer, bank, balance)   # call super constructor
        self._interest_rate = interest_rate
        
    def accrue_interest(self, interest_rate):
        """The saving account will pay interest based on balance and interest rate.
        """
        self.balance += interest_rate * balance     # call inherited method