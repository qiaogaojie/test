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
    ans = res[0]
    for i in range(ope):
        line = sys.stdin.readline().strip()
        line = list(map(int, line.split()))
        o = line[0]
        oo = line[1]
        if o == 1 and oo < n:
            ans = res[oo]
            n -= oo
            ind = oo
        elif o == 2 and n > 1 and oo in s:
            if oo == ans:
                ans = res[ind + 1]
                ss.remove(oo)
                n -= 1
        elif o == 3 and oo in s and (oo not in ss):
            n += 1
            ss.add(oo)
    print(ans)


           

if __name__ == "__main__":
    func()
