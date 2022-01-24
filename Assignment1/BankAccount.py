# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:50:01 2022

@author: Monica Li
"""

class BankAccount:
    """BankAccount must be an ‘abstract base class’.
    BankAccountmust be constructed with 3 arguments to __init__ which are:
        1. Name of the person who owns the bank account (string)
        2. Name of the bank (string)
        3. Initial balance (float)"""
        
    def __init__(self, customer, bank, balance):
        