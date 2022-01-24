from BankAccount import BankAccount
class ChequingAccount(BankAccount):
    """An extension to BankAccount that can make purchase with transaction fees implemented."""
    
    def __init__(self, customer, bank, balance, transaction_fee):
        """Create a new predatory credit card instance.
        The initial balance is zero.
        customer   the name of the customer
        bank       the name of the bank
        acnt       the account identifier
        limit      credit limit
        apr        annual percentage rate
        """
        
        super().__init__(customer, bank, balance)   # call super constructor
        self._transaction_fee = transaction_fee