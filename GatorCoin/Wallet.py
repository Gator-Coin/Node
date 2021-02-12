from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockUtils import BlockUtils


class Wallet():

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        dataHash = BlockUtils.hash(data)




#Test Run
if __name__ == '__main__':
    wallet = Wallet()
    print(wallet.keyPair)