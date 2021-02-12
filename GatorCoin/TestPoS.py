from ProofOfStake import ProofOfStake
from Lot import Lot

if __name__ == '__main__':
    ps = ProofOfStake()
    ps.update('Garret', 10)
    ps.update('Miggy', 30)
    ps.update('DonVito', 33)
    print(ps.get('Garrett'))
    print(ps.get('Miggy'))
    print(ps.get('DonVito'))
    print(ps.get('Jack'))

    lot = Lot('Daren', 1, 'lastHash')
    print(lot.lotHash())




