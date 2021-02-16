# please document code using this style
# https://docutils.sourceforge.io/rst.html


from time import time as timestamp
from uuid import uuid4 as generate_uuid
from hashlib import sha256
import json

class Ledger(dict):
    def __init__(self, file_path = None):
        """ 
        Creates a new Ledger object that cotains blocks, this should be a dict where the key is the hash of the block

        :param filename: loads from a file names relative or absolute path
        """
        self.pending_transactions = []
        if file_path:
            self.load(file_path)
        else:
            self = list()

    def add_transaction(self, sender, receiver, amount):
        """ 
        Adds a new transactions to the pending_transactions list. 
    
        The pending_transactions list are all the transactions on the
        network that need to be packed into the next block. 
    
        :param sender: public key of the sender
        :param receiver: private key of the receiver
        :param amount: Amount of curency being transacted 
    
        :returns: true if the transaction was added to the list else returns the error
        """
        self.pending_transactions.append(
            Transaction(sender, receiver, amount))

    def new_block(self, proof):
        """ 
        TODO: Create a new_block method
    
        :param proof: proof needs to be a byte object that can be hashed with the proof from the last block. 
    
        :returns: true if the block was created to

        :throws: Invalid proof
        """
        pass

    def save(self, file_path):
        """ 
        Overwrite a file with the blockchain
    
        :param file_path: reletive or absoulte path of the file to overwrite with the blockchain
    
        :returns: true if the file was saved

        :throws: IOError
        """
        json.dump(self, open(file_path, 'w'))


    def load(self, file_path):
        """ 
        Loads a json file containing the blockchain
    
        :param file_path: reletive or absoulte path of the file to overwrite with the blockchain
    
        :returns: true if the file was saved

        :throws: IOError
        """
        json.load(self, open(file_path, 'r'))

    def update(self, file_path):
        """ 
        TODO: Create a function that appends a file with blocks not yet added to file
        its important to make this work incrementally so when the file grows large the
        node isnt forced to store the entire blockchain in memory
    
        :param file_path: reletive or absoulte path of the file to overwrite with the blockchain
    
        :returns: true if the file was saved

        :throws: IOError
        """
        pass

class Block(dict):
    """ 
    Creates a new block object

    :param filename: loads from a file names relative or absolute path
    """
    def __init__(self, prev_hash, nonce, transactions):
        self["prev_hash"] = prev_hash
        self["nonce"] = nonce
        self["transactions"] = transactions
        self["timestamp"] = int(timestamp())

    def __json__(self):
        """ 
        :returns: the json representation of the block in the correct format to work with the hasing function
        """
        return json.dumps(self, indent=2, sort_keys=True)

    def hash(self):
        """ 
        :returns: a hexidecimal hash that is unique to the block
        """
        return sha256(self.__json__().encode("utf8")).hexdigest()


class Transaction(dict):
    def __init__(self, destination, signature, amount=0, fee=0):
        """
        This is a object that represents a transaction that will be loaded into a blockchain
        TODO:   * Cryptographically authenticate this based on a private key.
                * Encode and store this as raw bytes

        :param sender: the public key of the sender
        :param receiver: the public key of the receiver
        :param proof: the cryptographic evedence that the sender is the one who created the transaction.
        :param amount:  the amount of currency being sent to the receivers wallet.

        """
        self["txid"] = generate_uuid()
        self["destination"] = destination
        self["signature"] = signature
        self['amount'] = amount
        self['fee'] = fee

if __name__ == '__main__':
    ledger = Transaction()
