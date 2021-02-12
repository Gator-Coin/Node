from Block import Block
from Blockchain import Blockchain
from Wallet import Wallet
from TransactionPool import TransactionPool
from SocketCommunication import SocketCommunication


class Node():

    def __init__(self):
        #TODO self.transactionPool = TransactionPool()
        self.wallet          = Wallet()
        self.blockchain      = Blockchain()
        self.ip   = None#ip
        self.port = None#port
        self.transactionPool = TransactionPool()

    #TODO
    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)



