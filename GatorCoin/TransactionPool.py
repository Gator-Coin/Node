


class TransactionPool():

    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def transactionExists(self, tranaction):
        for poolTransaction in self.transactions:
            if poolTransaction.equals(tranaction)
                return True
        return False

    #TODO
    def removeFromPool(self, transaction):
        pass

    def forgerRequired(self):
        #If threshold in transactionpool is reached
        #It will signal time to build a new block
        #which also means it time to pick a new forger in the list of validators
        #
        if len(self.transactions) <=1:#This value can be altered and change
            return True
        else:
            return False




