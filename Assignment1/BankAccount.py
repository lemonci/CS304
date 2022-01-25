# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:50:01 2022

@author: Monica Li
"""

from abc import ABCMeta, abstractmethod         # need these because BankAccount 
                                                # must be an ‘abstract base class’
                                                
class BankAccount(metaclass=ABCMeta):
    """BankAccount must be an ‘abstract base class’.
    BankAccountmust be constructed with 3 arguments to __init__ which are:
        1. Name of the person who owns the bank account (string)
        2. Name of the bank (string)
        3. Initial balance (float)"""
    
    @abstractmethod
    def __init__(self, customer, bank, balance):
        self._customer = str(customer)
        self._bank = str(bank)
        self._balance = float(balance)
        
    def get_customer(self):
        """Return name of the customer."""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name."""
        return self._bank
    
    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if (self._balance - amount > 0):
            self._balance -= amount
            return True
        else:
            return False
            
    def __iadd__(self, amount):
        print(self._balance)
        self._balance += amount
        
    def __isub__(self, amount):
        self._balance -= amount
    
    def __lt__(self, accountB):
        return (self._balance < accountB.get_balance())
        
    def __gt__(self, accountB):
        return (self._balance > accountB.get_balance())