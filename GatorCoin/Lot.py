from BlockUtils import BlockUtils

class Lot():

    def __init__(self, publicKey, iteration, lastBlockHash):
        self.publicKey        = str(publicKey)
        self.iteration     = iteration #How many times we hash, dependent on stake
        self.lastBlockHash = lastBlockHash


    def lotHash(self):
        hashData=self.publicKey + self.lastBlockHash
        for _ in range(self.iteration):
            hashData = BlockUtils.hash(hashData).hexdigest()
        return hashData



