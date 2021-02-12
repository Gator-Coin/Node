# contains a linked list of blocks

import os
from hashlib import sha256
from lib2to3.pgen2.grammar import line
import random
import string
from Transaction import Transaction
from Block import Block
from Blockchain import Blockchain
from Wallet import Wallet






#Test Run
if __name__ == '__main__':
    print('PyCharm')

    #Testing Out if Signature really works
    #Testing Transaction
    sender   = 'sender'
    reciever = 'receiver'
    amount   = 1
    type     = 'TRANSFER'

    transaction = Transaction(sender, reciever, amount, type)
    print(transaction)
    print(transaction.toJson())

    #Testing Wallet
    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    transaction.sign(signature) #Comment out
    print(transaction.toJson())

    signatureValid = Wallet.signatureValid(transaction.toJson(), \
                                           signature, wallet.publicKeyString())
    ##TODO create a more valid working signature
    print(signatureValid)# This is dependent on signature being commented out-> not the same information to create the hash






    #Test 2.11.2021
    #Initial Blockchain
    #blockChain= Blockchain()# Great the block chain
    #blockChain.blockchain.append(blockChain.mineBlock(blockChain.blockchain[-1]))
    #[print(x) for x in blockChain.blockchain]#Print all blocks with information





    # hashedWord = sha256(line.encode('utf-8')).hexdigest()
    # print(hashedWord)
    # [print(sha256().hexdigest()) for _ in  range(10) ]
    # import random
    # import string
    # import hashlib
    #
    # random.seed(1)
    #
    # for i in range(5):
    #     data = ''.join(random.choice(string.ascii_uppercase + string.digits)
    #                    for _ in range(10))
    #
    #     hashed = hashlib.sha256()
    #     hashed.update(data.encode('ascii'))
    #     print(data, "->", sha256(data.encode('ascii')).hexdigest())
    #
    #
