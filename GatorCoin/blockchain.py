# please document code using this style
# https://docutils.sourceforge.io/rst.html


from time import time as timestamp
from hashlib import sha256
import json

class Ledger(list):
    def __init__(self):
        self.pending_transactions = []

    def add_transaction(self, sender, receiver, amount):
    """ 
    Adds a new transactions to the pending_transactions list. 
  
    The pending_transactions list are all the transactions on the
    network that need to be packed into the next block. 
  
    Parameters: 
    sender (key): public key of the sender
    receiver(key): private key of the receiver
    amount(int): Amount of curency being transacted 
  
    Returns: 
    int : 0  
  
    """
        self.pending_transactions.append(
            Transaction(sender, receiver, amount))

    def new_block(self, proof):
        pass

    def save(self, file_path):
        json.dump(self, open(file_path, 'w'))

    def load(self, file_path):
        json.load(self, open(file_path, 'r'))


class Block(dict):
    def __init__(self, proof, transactions):
        self["proof"] = proof
        self["transactions"] = transactions
        self["timestamp"] = str(timestamp())

    def json(self):
        return json.dumps(self, indent=2, sort_keys=True)

    def hash(self):
        return sha256(self.json().encode("utf8")).hexdigest()


class Transaction(dict):
    def __init__(self, sender, receiver, amount):
        self["sender"] = sender
        self["receiver"] = receiver
        self["amount"] = amount
        self["timestamp"] = str(timestamp())

if __name__ == '__main__':
    ledger = Ledger()
    ledger.add
