from Crypto.Hash import SHA256
import json


class BlockUtils():

    @staticmethod
    def hash(data):
        dataStringed = json.dumps(data)
        dataBytes    = dataStringed.encode('utf-8')
        dataHash     = SHA256.new(dataBytes)
        return dataHash


