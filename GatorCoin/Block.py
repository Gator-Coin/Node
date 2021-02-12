from datetime import datetime, timedelta
from hashlib import sha256
from lib2to3.pgen2.grammar import line



# contains transation, hash, and previous hash
# index and time
class Block():
    def __init__(self, index: int, hash: str, previousHash: str, timestamp: datetime, data: str):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = datetime.utcnow()#timestamp
        self.data = data
        self.hash = hash

    def __str__(self):
        index = "Index: "+str(self.index)+"\n"
        prevHash = "Previous Hash: "+str(self.previousHash)+"\n"
        #self.timestamp = datetime.utcnow()  # timestamp ##TODO fix time stamp
        #self.data = data##TODO add real data, will this be transactions as well?
        hash = "Hash: " + str(self.hash) + "\n"
        return index+ prevHash + hash
