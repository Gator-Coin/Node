from hashlib import sha256 as magic

import datetime


class BlockUtils:
  @staticmethod
  def hash(data):
    return magic((datetime.datetime.now().strftime("%H:%M:%S")).encode('utf-8')).hexdigest()

class Blockchain(object):
    def __init__(self, val, next=None):
        self.block = val
        self.next = next

# block object is list
class Block(list):
    def __init__(self, previousHash):
        self.hash = BlockUtils.hash(previousHash) 
        self.previous = previousHash
        pass
    
    def addTransaction(self,transaction):
        self.append(transaction)

# transaction object
class Transaction(object):
    def __init__(self, sender, reciever, amount):
        self.sender    = sender
        self.reciever  = reciever
        self.amount    = amount
        self.transTime = datetime.datetime.now()
        self.id        = magic((sender+reciever).encode('utf-8')).hexdigest() 


# Test Run 
if __name__ == '__main__':
  genBlock = Block(0)
  t1 = Transaction("Sender", "Reciever", 300)
  t2 = Transaction("Jade", "Miguel", 900)
  t3 = Transaction("Dustin", "Zach", 1500)
  genBlock.addTransaction(t1)
  genBlock.addTransaction(t2)
  genBlock.addTransaction(t3)
  blockchain = Blockchain(genBlock)
  
  for b in blockchain:
    print(b)


