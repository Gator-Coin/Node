from Block import Block
from Blockchain import Blockchain



class Node():

    def __init__(self):
        self.transactionPool = TransactionPool()
        self.wallet          = Wallet()
        self.blockchain      = Blockchain()
