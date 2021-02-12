from ProofOfStake import ProofOfStake
from Lot import Lot
import string
import random


def generateRandomStrings(length):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(length))
    return resultString



if __name__ == '__main__':
    ps = ProofOfStake()
    ps.update('Garret', 200)
    ps.update('Miggy', 30)
    ps.update('DonVito', 33)
    print(ps.get('Garrett'))
    print(ps.get('Miggy'))
    print(ps.get('DonVito'))
    print(ps.get('Jack'))

    garrettWins = 0
    miggyWins   = 0
    DonVitoWins = 0

    for i in range(1000):
        forger = ps.forger(generateRandomStrings(i))
        if forger == 'Garrett':
            garrettWins+=1
        elif forger == 'Miggy':
            miggyWins+=1
        elif forger == "DonVito":
            DonVitoWins+=1

    print("Garrett won "+str(garrettWins) + " times")
    print("Miggy won " + str(miggyWins) + " times")
    print("DonVito won " + str(DonVitoWins) + " times")







    lot = Lot('Daren', 1, 'lastHash')
    print(lot.lotHash())







