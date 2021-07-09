# please document code using this style
# https://docutils.sourceforge.io/rst.html
"""
This file contains all of the data structures required to make a working blockchain. 
"""
from crypto import Key_Ring
from time import time as timestamp
from hashlib import sha256
from time import time_ns
import json


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

    def add_transaction(self, inputs: list, outputs: list, signature: bytes):
        """ 
        Adds a new transactions to the pending_transactions list. 
    
        The pending_transactions list are all the transactions on the
        network that need to be packed into the next block. 
    
        :param inputs: the transactions to an address
        :param outputs: the address of the recivers 
        :param signature: the signature of the sender 
    
        :throws: invalid transaction if the transaction is not valid.
        """
        self.pending_transactions.append(
            Transaction(inputs, outputs))

    def new_block(self, proof: bytes):
        """ 
        TODO: Create a new_block method
    
        :param proof: proof needs to be a byte object that can be hashed with the proof from the last block. 
    
        :returns: true if the block was created to

        :throws: Invalid proof
        """
        pass

    def save(self, file_path: str):
        """ 
        Overwrite a file with the blockchain
    
        :param file_path: reletive or absoulte path of the file to overwrite with the blockchain
    
        :returns: true if the file was saved

        :throws: IOError
        """
        json.dump(self, open(file_path, 'w'))


    def load(self, file_path: str):
        """ 
        Loads a json file containing the blockchain
    
        :param file_path: reletive or absoulte path of the file to overwrite with the blockchain
    
        :returns: true if the file was saved

        :throws: IOError
        """
        json.load(self, open(file_path, 'r'))

    def update(self, file_path: str):
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

    def __init__(self, prev_hash: bytes, nonce: bytes, transactions: list, network_identifier: bytes):
        """ 
        Creates a new block object
        
        :param prev_hash: The hash of the last block.
        :param network_identifier: this is used to identify which block chain this block is part of. 
        :param nonce: This is a number used to alter the hash of the block to something determined valid by the block difficulty
        :param transactions: A list of transactions that needs to be added to the block. 
         """
        
        self["network_identifier"] = network_identifier
        self["prev_hash"] = prev_hash
        self["nonce"] = nonce
        self["transactions"] = transactions
        self["timestamp"] = int(timestamp())

    def __json__(self) -> str:
        """ 
        :returns: the json representation of the block in the correct format to work with the hasing function
        """
        return json.dumps(self, indent=2, sort_keys=True)

    def hash(self) -> str:
        """ 
        :returns: a hexidecimal hash that is unique to the block
        """
        return sha256(self.__json__().encode("utf8")).hexdigest()


class Transaction(dict):
    def __init__(self, inputs: list, outputs: list, key: Key_Ring):
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
        self["public_key"] = key.public_bytes().decode()
        self["inputs"] = self.tx_inputs(inputs)
        self["outputs"] = self.tx_outputs(outputs)

    @staticmethod
    def validate_transactions(self) -> bool:
            """
            TODO: * Validate that transaction inputs have enough currency to support the output transactions
            """
            return True

    def sign(self, key: Key_Ring) -> bytes:
        """
        TODO: Implement signing the transaction with the private key to generate a signature
        """
        return key.sign(self.serialize())
        
    @classmethod
    def __str__(self):
        return super().__str__()

    @classmethod
    def serialize(self) -> bytes:
            """
            This should return the serialized bytes representing the transaction

            :returns: the serialized bytes

            """
            return json.dumps(self, sort_keys=True).encode("utf8")

    @staticmethod
    def deserialize(bytes: bytes) -> "Transaction":
            """
            This should a transaction from serialized bytes

            :param bytes: a transaction
            """
            return json.loads(bytes)
            

    class tx_inputs(list):
        def __init__(self, inputs: list):
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
        def validate(tx_id: bytes) -> bool :
            """
            TODO: Validate addresses to be correct format
            """
            return True

        def __str__(self) -> str:
            return json.dumps(self)

    class tx_outputs(list):
        """
        This inner class exists as a way to provide error checking to make sure all out transactions are valid signatures amount pairs

        :param inputs: a list of all transactions used as an inputs

        """
        def __init__(self, destinations: list):
            for address, amount in destinations:
                if(self.validate(address, amount)):
                    self.append((address, amount))
                else:
                    raise TypeError(f"{(address, amount)} could not be converted to a destination address")

        @staticmethod
        def validate(address: bytes, amount: int) -> bool:
            """
            TODO: Validate addresses to be correct format
            """
            return True

        def __str__(self) -> str:
            return json.dumps(self)


if __name__ == '__main__':
    key = Key_Ring()
    key.generate()

    tx = Transaction([1234], [(5,2)], key)
    print(json.dumps(tx))

