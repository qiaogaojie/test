import sys
n = int(input())
line = sys.stdin.readline().strip()
line = list(map(int, line.split()))
m = int(input())
line2 = sys.stdin.readline().strip()
line2 = list(map(str, line2.split()))

t = [int(line2[2*i]) for i in range(m)]
o = [line2[2*i + 1] for i in range(m)]
ans = []
s = sum(line)
for i in range(m):
    res = s
    tt = t[i] - 1
    oo = o[i]
    if oo == "-":
        res -= 2 * line[tt + 1]
    elif oo == "*":
        res = res + line[tt] * line[tt + 1] - line[tt] - line[tt + 1]
    elif oo == "/":
        res = res + line[tt] / line[tt + 1] - line[tt] - line[tt + 1]
    ans.append(res)
ans = [str(round(float(a), 1)) for a in ans]
print(" ".join(ans))