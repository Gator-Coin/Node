from Crypto.PublicKey import RSA


class Wallet():

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, sign):
        pass




#Test Run
if __name__ == '__main__':
    wallet = Wallet()
    print(wallet.keyPair)