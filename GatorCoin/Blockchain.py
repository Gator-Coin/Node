from datetime import datetime, timedelta
import Block
from hashlib import sha256
from lib2to3.pgen2.grammar import line

from BlockUtils import BlockUtils
from ProofOfWork import ProofOfWork
from ProofOfWork import ProofOfStake

#TODO make this a linklist
class Blockchain():
    def __init__(self):
        self.blockchain=[]
        self.genisis=Block(0, sha256(line.encode('utf-8')).hexdigest(), None, datetime.utcnow(), 'my genesis block!!')
        self.blockchain.append(self.genisis)
        self.DIFFICULTY=1
        #TODO edit this so, upon instializing Blockchain it can be made into PoW or PoS or PoSomething
        self.PROOFof=ProofOfWork()


    def recreateHash(self, block):
        return BlockUtils.calculateHash(block.timestamp, block.previousHash, block.data)



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



# Test Run
if __name__ == '__main__':

    #Initial Blockchain Test
    #Last Test 2.11.2021 12:00pm
    blockChain= Blockchain()# Great the block chain
    blockChain.blockchain.append(blockChain.mineBlock(blockChain.blockchain[-1]))
    [print(x) for x in blockChain.blockchain]#Print all blocks with information

