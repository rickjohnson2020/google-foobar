from itertools import combinations

def solution(L):
    L.sort(reverse = True)
    for i in reversed(range(1, len(L) + 1)):
        for tup in list(combinations(L, i)):
            if sum(tup) % 3 == 0: return int(''.join(map(str, tup)))
    return 0
