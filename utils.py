import math
import time
import sys
import bisect
import numpy as np


def sigmoid(x):
    if x >= 0:
        return math.exp(-np.logaddexp(0, -x))
    else:
        return math.exp(x - np.logaddexp(x, 0))


def load_check_ins(check_in_file, t=6):
    times = []
    users = []
    axis_xs = []
    axis_ys = []
    locations = []
    S = []
    L = {}
    for line in check_in_file:
        params = line.strip().split()
        users.append(int(params[0]))
        times.append(time.mktime(time.strptime(params[1], '%Y-%m-%dT%H:%M:%SZ')))
        axis_xs.append(float(params[2]))
        axis_ys.append(float(params[3]))
        locations.append(int(params[4]))
    interval = compute_interval(times, t)
    for i in range(len(users)):
        u_id = users[i]
        l_id = locations[i]
        t_index = bisect.bisect(interval, times[i]) - 1
        S.append((u_id, t_index, l_id))
        if u_id not in L:
            L[u_id] = [[] for i in range(t)]
        try:
            L[u_id][t_index].append(l_id)
        except IndexError:
            print t_index
    return S, L


def compute_interval(times, t):
    max_stamp = 0
    min_stamp = sys.maxint
    for i in range(len(times)):
        timestamp = times[i]
        max_stamp = max(max_stamp, timestamp)
        min_stamp = min(min_stamp, timestamp)
    in_l = (max_stamp - min_stamp) / 6
    time_interval = [min_stamp + in_l*i for i in range(t+1)]
    return time_interval
