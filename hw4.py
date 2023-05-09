import sys
import collections
def func():
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    res = list(range(line[0], line[-1] + 1))
    d = collections.deque(res)
    s = set(res)
    ss = set(res)
    ope = int(input())
    n = len(res)
    for i in range(ope):
        line = sys.stdin.readline().strip()
        line = list(map(int, line.split()))
        o = line[0]
        oo = line[1]
        if o == 1 and oo < n:
            n -= oo
            ind = oo
            for i in range(oo):
                ss.remove(d.popleft())
        elif o == 2 and n > 1 and oo in s:
            ss.remove(oo)
            d.remove(oo)
            n -= 1
        elif o == 3 and oo in s and (oo not in ss):
            n += 1
            ss.add(oo)
            d.append(oo)
    print(d[0])
