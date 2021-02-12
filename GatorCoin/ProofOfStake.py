from BlockUtils import BlockUtils
from Lot import Lot

class ProofOfStake:

    #It keep track of amount VS stake
    def __init__(self):
        self.stakers= {}#Dictonary Key is amount, value is stake
        pass

    #update the amount of stake
    def update(self, publicKeyString, stake):
        if publicKeyString in self.stakers:
            self.stakers[publicKeyString] += stake
        else:
            self.stakers[publicKeyString] = stake

    def get(self, publicKeyString):
        if publicKeyString in self.stakers:
            return self.stakers[publicKeyString]
        else:
            return None


    def validatorLots(self, seed):
        lots = []
        for validator in self.stakers.keys():
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake+1, seed))
        return lots


    def winnerLot(self, lots, seed):
        winnerLot   = None
        leastOffSet = None
        referenceHashIntValue = int(BlockUtils.hash(seed).hexdigest(), 16) #last arguement is size
        for lot in lots:
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue - referenceHashIntValue)
            if leastOffSet is None or offset < leastOffSet:
                leastOffSet = offset
                winnerLot = lot
        return winnerLot


    def forger(self, lastBlockHash):
        lots = self.validatorLots(lastBlockHash)
        winnerLot = self.winnerLot(lots, lastBlockHash)
        return winnerLot.publicKey



