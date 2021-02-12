from Block import Block
from Blockchain import Blockchain
from Wallet import Wallet


class Node():

    def __init__(self):
        #TODO self.transactionPool = TransactionPool()
        self.wallet          = Wallet()
        self.blockchain      = Blockchain()
