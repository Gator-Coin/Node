# contains a linked list of blocks

import os
from hashlib import sha256
from lib2to3.pgen2.grammar import line
import random
import string
from Transaction import Transaction
from Block import Block
from Blockchain import Blockchain







#Test Run
if __name__ == '__main__':
    print('PyCharm')
    sender   = 'sender'
    reciever = 'receiver'
    amount   = 1
    type     = 'TRANSFER'

    transaction = Transaction(sender, reciever, amount, type)
    print(transaction)
    print(transaction.toJson())





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
