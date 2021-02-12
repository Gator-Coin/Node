from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockUtils import BlockUtils


class Wallet():

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        dataHash             = BlockUtils.hash(data)
        signatureSchemObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemObject.sign(dataHash)
        return signature.hex()

    @staticmethod
    def signatureValid(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash  = BlockUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureScheme  = PKCS1_v1_5.new(publicKey)
        signatureValid   = signatureScheme.verify(dataHash, signature)
        return signatureValid


    def publicKeyString(self):
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString




#Test Run
if __name__ == '__main__':
    wallet = Wallet()
    print(wallet.keyPair)