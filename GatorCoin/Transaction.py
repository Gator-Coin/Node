import uuid
import time

"""TODO/ random thought, Immutability?, especially of something like gensis block?"""
# contains send reciever amount time hash

class Transaction():

    def __init__(self, senderPublicKey, recieverPublicKey, amount, type):
        self.senderPublicKey    = senderPublicKey
        self.recieverPublicKey  = recieverPublicKey
        self.amount             = amount
        self.type               = type
        self.id                 = uuid.uuid1().hex
        self.timestamp          = time.time()
        self.signature          = ''


    def toJson(self):
        return self.__dict__




