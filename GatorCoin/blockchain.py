# please document code using this style
# https://docutils.sourceforge.io/rst.html
"""
This file contains all of the data structures required to make a working blockchain. 
"""
from time import time as timestamp
from hashlib import sha256
from cryptography import *
import json
import os

class Ledger(dict):
    def __init__(self, file_path = None):
        """ 
        Creates a new Ledger object that cotains blocks, this should be a dict where the key is the hash of the block

        :param filename: loads from a file names relative or absolute path
        """
        self.pending_transactions = []
        self.current_block = Block()
        if file_path:
            self.load(file_path)
        else:
            self = list()

    def add_transaction(self, inputs, outputs, signature):
        """ 
        Adds a new transactions to the pending_transactions list. 
    
        The pending_transactions list are all the transactions on the
        network that need to be packed into the next block. 
    
        :param inputs: the transactions to an address
        :param outputs: the address of the recivers 
        :param signature: the signature of the sender 
    
        :returns: true if the transaction was added to the list else returns the error
        """
        self.pending_transactions.append(
            Transaction(inputs, outputs, signature))

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

    def __init__(self, prev_hash, nonce, transactions):
        """ 
        Creates a new block object

        :param filename: loads from a file names relative or absolute path
        :param nonce: This is a number used to alter the hash of the block to something determined valid by the block difficulty
         """
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
    def __init__(self, inputs, outputs, signature):
        """
        This is a object that represents a transaction that will be loaded into a blockchain
        TODO:   * Cryptographically authenticate this based on a private key.
                * Encode and store this as raw bytes
                * A transaction needs to have multiple inputs and outputs

        :param inputs: a list of all transactions used as an inputs
        :param outputs: a dict of {destinations: amount} pairs that corrispond to the destinations 
        :param proof: the cryptographic evedence that the sender is the one who created the transaction.
        :param amount:  the amount of currency being sent to the receivers wallet.

        """
        self["inputs"] = self.tx_inputs(inputs)
        self["outputs"] = self.tx_outputs(outputs)
        self["signature"] = self.sign()

    @staticmethod
    def validate_transactions(self):
            """
            TODO:   * Validate that transaction inputs have enough currency to support the output transactions
            """
            return True

    def sign(self):
        """
        TODO: Implement signing the transaction with the private key to generate a signature
        """
        key = "some_key"
        return key

    def __json__(self):
            return json.dumps(self)

    def __str__(self):
        n = "\n"
        return f'Inputs:\n {"".join(str(self["inputs"]) + n)}Outputs:{n}{"".join(str(self["outputs"])) + n}Signature: {self["signature"]}'

    class tx_inputs(list):
        def __init__(self, inputs):
            """
            This inner class exists as a way to provide error checking to make sure all input transactions are valid signatures

            :param inputs: a list of all transactions used as an inputs

            """
            for tx_id in inputs:
                if(self.validate(tx_id)):
                    self.append(tx_id)
                else:
                    raise TypeError(f"{tx} could not be converted to a tx_input")
        
        @staticmethod
        def validate(tx_id):
            """
            TODO: Validate addresses to be correct format
            """
            return True

        def __str__(self):
            return json.dumps(self)

    class tx_outputs(list):
        """
        This inner class exists as a way to provide error checking to make sure all out transactions are valid signatures amount pairs

        :param inputs: a list of all transactions used as an inputs

        """
        def __init__(self, destinations):
            for address, amount in destinations:
                if(self.validate(address, amount)):
                    self.append((address, amount))
                else:
                    raise TypeError(f"{(address, amount)} could not be converted to a destination address")

        @staticmethod
        def validate(address, amount):
            """
            TODO: Validate addresses to be correct format
            """
            return True

        def __str__(self):
            return json.dumps(self)


if __name__ == '__main__':
    tx = Transaction([1234], [(5,2)], "signature")

