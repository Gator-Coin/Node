from datetime import datetime

from Crypto.Hash import SHA256
import json


class BlockUtils():

    @staticmethod
    def hash(data):
        dataStringed = json.dumps(data)
        dataBytes    = dataStringed.encode('utf-8')
        dataHash     = SHA256.new(dataBytes)
        return dataHash


    @staticmethod
    def calculateHash(timestamp, lastHash, data):
        time =  datetime.utcnow()
        data= str(time.timestamp())+", "+lastHash+", "+data
        return sha256(data.encode('ascii')).hexdigest()

