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
        
    def accrue_interest(self):
        """The saving account will pay interest based on balance and interest rate.
        """
        self._balance += self._interest_rate * self._balance     # call inherited method
        
#Testing        
if __name__ == '__main__':
    wallet = []
    wallet.append(SavingsAccount('John Bowman', 'California Saving',
                              2500, 0.01))
    wallet.append(SavingsAccount('John Bowman', 'California Federal',
                              3500, 0.02))
    wallet.append(SavingsAccount('John Bowman', 'California Finance',
                              5000, 0.05))
    
    for c in range(3):
        print('Card %d : ' %(c+1))
        print('Bank =', wallet[c].get_bank())
        print('Customer =', wallet[c].get_customer())
        print('Original Balance =', wallet[c].get_balance())
        
    print('Card 1 Balance > Card 2 Balance: ', wallet[0] > wallet[1])
    print('Card 2 Balance > Card 3 Balance: ',wallet[1] > wallet[2])
    print('Card 3 Balance > Card 1 Balance: ',wallet[2] > wallet[0])
    
    print('Card 1 Balance < Card 2 Balance: ', wallet[0] < wallet[1])
    print('Card 2 Balance < Card 3 Balance: ',wallet[1] < wallet[2])
    print('Card 3 Balance < Card 1 Balance: ',wallet[2] < wallet[0])

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
    
    for i in range(1, 3):
        wallet[0].accrue_interest()
        wallet[1].accrue_interest()
        wallet[2].accrue_interest()
        for c in range(3):
            print('Card %d : Balance after period %d interest payment =' %(c+1, i), wallet[c].get_balance())