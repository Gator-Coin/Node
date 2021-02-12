class ProofOfWork:
    def __init__(self):
        pass


    # TODO make a Unit-Test for this, has yet been tested
    #@staticmethod
    def isValidChain(self, thisBlockList, chain):
        # TODO double check if this is a shallow copy or deep copy comparison
        if thisBlockList[0] !=chain[0]: return False
        # TODO this is terrible logic, in the case of some blocks not being the same length or vary by multiple blocks
        for i in  range(1,  len(chain) )  :  # Iterate through entire new chain
            if len(thisBlockList ) >i  :  # if our block is smaller we do not index past it
                if str(thisBlockList[i] ) !=str(chain[i]): return False  # if they are not the same, something is wrong
            lastBlock = chain[ i -1]
            curBlock  = chain[i]
            #TODO choose a hashing method used, I learnt one way and swtich to another way. Need to change the below code so everything mathvches
            if lastBlock.hash != curBlock.previousHash or \
                    curBlock.hash != thisBlock.calculateHash(curBlock.time, lastBlock.hash, "NotSureYet"):
                return False
        return True


    # Note should probably make this return True/False
    def replaceChain(self, thisBlockList, chain):
        if len(chain) <= len(thisBlockList):
            print("Chain is not longer than the current chain")
            return
        elif False == self.isValidChain(chain)  :  # Very redundant but I did that for you, the reader
            print("chain is not valid")
            return
        else:
            print("Attempting to replacing chain")
            try:
                return chain
            except:
                print("Chain update Failed")