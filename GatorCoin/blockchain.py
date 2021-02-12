from datetime import datetime, timedelta
import Block
from hashlib import sha256
from lib2to3.pgen2.grammar import line

#TODO make this a linklist
class Blockchain():
    def __init__(self):
        self.blockchain=[]
        self.genisis=Block(0, sha256(line.encode('utf-8')).hexdigest(), None, datetime.utcnow(), 'my genesis block!!')
        self.blockchain.append(self.genisis)
        self.DIFFICULTY=1


    def recreateHash(self, block):
        return self.calculateHash(block.timestamp, block.previousHash, block.data)

    def calculateHash(self, timestamp, lastHash, data):
        time =  datetime.utcnow()
        data= str(time.timestamp())+", "+lastHash+", "+data
        return sha256(data.encode('ascii')).hexdigest()

    def mineBlock(self, lastBlock):
        now =  datetime.utcnow()##TODO check if the correct use of time
        hash = self.calculateHash(now, lastBlock.hash, "NotSureYet")

        ###TODO implement a check here? if things are valid
        return Block(len(self.blockchain), hash, lastBlock.hash, datetime.utcnow(), "yetTomake")

    def hashMatchesDifficulty(self, hash, difficulty) -> bool:
        stringedHash     = str(hash)
        for i in range(0,difficulty):
            if stringedHash[i]!='0': return False
        return True


    def findBlock(self, index, previousHash, timestamp, data, difficulty):
        nonce = 0
        while True:
            hash = self.calculateHash(index, previousHash, timestamp, data, difficulty, nonce)
            if self.hashMatchesDifficulty(hash, difficulty):
                return Block(index, hash, previousHash, timestamp, data, difficulty, nonce)
            nonce+=1


    #TODO make a Unit-Test for this, has yet been tested
    @staticmethod
    def isValidChain(self, chain):
        #TODO double check if this is a shallow copy or deep copy comparison
        if self.genisis!=chain[0]: return False
        #TODO this is terrible logic, in the case of some blocks not being the same length or vary by multiple blocks
        for i in  range(1,  len(chain) ):#Iterate through entire new chain
            if len(self.blockchain)>i:#if our block is smaller we do not index past it
                if str(self.blockchain[i])!=str(chain[i]): return False#if they are not the same, something is wrong
            lastBlock = chain[i-1]
            curBlock  = chain[i]
            if lastBlock.hash != curBlock.previousHash or \
                    curBlock.hash != self.calculateHash(curBlock.time, lastBlock.hash, "NotSureYet"):
                    return False
        return True


    #Note should probably make this return True/False
    def replaceChain(self, chain):
        if len(chain) <= len(self.blockchain):
            print("Chain is not longer than the current chain")
            return
        elif False==self.isValidChain(chain):#Very redundant but I did that for you, the reader
            print("chain is not valid")
            return
        else:
            print("Attempting to replacing chain")
            try:
                self.blockchain=chain
            except:
                print("Chain update Failed")


# Test Run
if __name__ == '__main__':

    #Initial Blockchain Test
    #Last Test 2.11.2021 12:00pm
    blockChain= Blockchain()# Great the block chain
    blockChain.blockchain.append(blockChain.mineBlock(blockChain.blockchain[-1]))
    [print(x) for x in blockChain.blockchain]#Print all blocks with information

