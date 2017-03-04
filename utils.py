import math
import time
import cPickle as pickle
import numpy as np

seconds_an_hour = 3600


def sigmoid(x):
    if x >= 0:
        return math.exp(-np.logaddexp(0, -x))
    else:
        return math.exp(x - np.logaddexp(x, 0))


def load_check_ins(check_in_file, h=6):
    amended_ids = []
    amended_index = -1
    check_ins = []
    coordinates = {}
    L = []
    S = []
    interval = h * seconds_an_hour
    for line in check_in_file:
        params = line.strip().split()
        u_id = int(params[0])
        t = time.mktime(time.strptime(params[1], '%Y-%m-%dT%H:%M:%SZ'))
        axis_xs = float(params[2])
        axis_ys = float(params[3])
        loc_id = int(params[4])
        if u_id not in amended_ids:
            amended_ids.append(u_id)
            check_ins.append([])
            amended_index += 1
            if amended_index % 10000 == 0:
                print amended_index
        # if len(amended_ids) == 101:
        #     break
        coordinates[loc_id] = (axis_xs, axis_ys)
        # if u_id not in check_ins:
        #     check_ins[u_id] = []
        check_ins[amended_index].append((t, loc_id))
    for amended_id in range(len(check_ins)):
        check_ins[amended_id].reverse()
        # if u_id not in L:
        #     L[u_id] = {}
        # amended_id = amended_ids.index(u_id)
        if amended_id >= len(L):
            L.append([])
        t_index = 0
        infimum = -1
        for i in range(len(check_ins[amended_id])):
            t = check_ins[amended_id][i][0]
            if infimum == -1:
                infimum = t
            if t - infimum > interval:
                t_index += 1
                infimum = t
            # if t_index not in L[u_id]:
            #     L[u_id][t_index] = []
            if t_index >= len(L[amended_id]):
                L[amended_id].append([])
            loc_id = check_ins[amended_id][i][1]
            L[amended_id][t_index].append(loc_id)
            S.append((amended_id, t_index, loc_id))
    # for amended_id in range(len(L)):
    #     for t_index in range(len(L[amended_id])):
    #         for loc_id in L[amended_id][t_index]:
    #             S.append((amended_id, t_index, loc_id))
    return S, L

if __name__ == '__main__':
    with open('datasets/Gowalla/Gowalla_totalCheckins.txt') as f:
        S, L = load_check_ins(f)
    with open('data/S', 'w+') as f:
        pickle.dump(S, f)
    with open('data/L', 'w+') as f:
        pickle.dump(L, f)
