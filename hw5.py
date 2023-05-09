import sys
import collections
def func():    
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    left = line[0]
    right = line[-1]
    res = list(range(line[0], line[-1] + 1))
    d = collections.deque(res)
    s = set(res)
    ss = set(res)
    ope = int(input())
    n = len(res)
    de = set()
    for i in range(ope):
        line = sys.stdin.readline().strip()
        line = list(map(int, line.split()))
        o = line[0]
        oo = line[1]
        if o == 1 and oo < n:
            n -= oo
            new_left = left + oo
            for dd in de:
                if dd < left + oo and dd >= left:
                    new_left += 1
            left = new_left                    
            for i in range(oo):
                ss.remove(d.popleft())
        elif o == 2 and n > 1 and oo in s:
            ss.remove(oo)
            d.remove(oo)
            de.append(oo)
            n -= 1
        elif o == 3 and oo in s and (oo not in ss):
            n += 1
            ss.add(oo)
            d.append(oo)
    print(d[0])


           

if __name__ == "__main__":
    func()
