import pickle
from utils import *

if __name__ == '__main__':
    cif = open('datasets/Gowalla/Gowalla_totalCheckins.txt')
    S, L = load_check_ins(cif)
    Sf = open('data/S', 'w+')
    Lf = open('data/L', 'w+')
    pickle.dump(S, Sf)
    pickle.dump(L, Lf)

