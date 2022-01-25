from BankAccount import BankAccount
class ChequingAccount(BankAccount):
    """An extension to BankAccount that can make purchase with transaction fees implemented."""
    
    def __init__(self, customer, bank, balance, transaction_fee):
        """Create a chequing account instance.
        customer               the name of the customer
        bank                   the name of the bank
        balance                the account balance
        transaction_fee        the transaction fee during purchases
        """
        
        super().__init__(customer, bank, balance)     # call super constructor
        self._transaction_fee = transaction_fee
        
    def make_purchase(self, amount):
        """Charge given price to the card, assuming sufficient card balance.
        
        Return False if charge was not processed.
        Return True and assess transaction fees if charge is proceeded.
        """
        success = super().withdraw(amount)            # call inherited method
        if not success:
            self._balance -= self._transaction_fee    # assess transaction fee
        return success                                # caller expects return value

#Testing        
if __name__ == '__main__':
    wallet = []
    wallet.append(ChequingAccount('John Bowman', 'California Saving',
                              2500, 5))
    wallet.append(ChequingAccount('John Bowman', 'California Federal',
                              3500, 100))
    wallet.append(ChequingAccount('John Bowman', 'California Finance',
                              5000, 500))
    
    print('Card 1 Balance > Card 2 Balance: ', wallet[0] > wallet[1])
    print('Card 2 Balance > Card 3 Balance: ',wallet[1] > wallet[2])
    print('Card 3 Balance > Card 1 Balance: ',wallet[2] > wallet[0])
    
    print('Card 1 Balance < Card 2 Balance: ', wallet[0] < wallet[1])
    print('Card 2 Balance < Card 3 Balance: ',wallet[1] < wallet[2])
    print('Card 3 Balance < Card 1 Balance: ',wallet[2] < wallet[0])
    
    for c in range(3):
        print('Bank =', wallet[c].get_bank())
        print('Customer =', wallet[c].get_customer())
        print('Original Balance =', wallet[c].get_balance())

    for val in range(1, 5):
        wallet[0] += val*0.3
        wallet[1] += val*1.25
        wallet[2] += val*4.5

    for c in range(3):
        print('Card %d : Balance after addition =' %(c+1), wallet[c].get_balance())

    for val in range(1, 3):
        wallet[0] -= val * 0.3
        wallet[1] -= val * 1.25
        wallet[2] -= val * 4.5
        
    for c in range(3):
        print('Card %d : Balance after subtraction =' %(c+1), wallet[c].get_balance())

    for val in range(1, 3):
        wallet[0].deposit(val)
        wallet[1].deposit(15*val)
        wallet[2].deposit(100*val)    

    for c in range(3):
        print('Card %d : Balance after deposit =' %(c+1), wallet[c].get_balance())
    
    for val in range(1, 4):
        wallet[0].withdraw(2*val)
        wallet[1].withdraw(17*val)
        wallet[2].withdraw(200*val)   
    
    for c in range(3):
        print('Card %d : Balance after withdraw =' %(c+1), wallet[c].get_balance())
    
    for val in range(1, 2):
        wallet[0].make_purchase(val)
        wallet[1].make_purchase(20*val)
        wallet[2].make_purchase(300*val)
        
    for c in range(3):
        print('Card %d : Balance after purchase =' %(c+1), wallet[c].get_balance())