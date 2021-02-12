

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



