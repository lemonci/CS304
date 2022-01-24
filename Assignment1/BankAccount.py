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
       
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if (self.balance - amount > 0):
            self.balance -= amount
            return True
        else:
            return False
            
    def __iadd(self, amount)__:
        self.balance += amount
        
    def __isub(self, amount)__:
        self.balance -= amount
    
    def __lt__(self, accountB):
        return (self.amount < accountB.amount)
        
    def __gt__(self, accountB):
        return (self.amount > accountB.amount)