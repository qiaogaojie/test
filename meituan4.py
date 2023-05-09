import sys
n = int(input())
line1 = sys.stdin.readline().strip()
x = list(map(int, line1.split()))
line2 = sys.stdin.readline().strip()
y = list(map(int, line2.split()))
line3 = sys.stdin.readline().strip()
z = list(map(int, line3.split()))
m = int(input())
line4 = sys.stdin.readline().strip()
q = list(map(int, line4.split()))
ans = []
c = [x[i] - y[i] for i in range(n)]

for i in range(m):
    qq = q[i] - 1
    if qq == 0:
        ans.append(c[0] * z[0])
        continue
    cc = c[qq]
    minn = cc * z[qq]
    j = qq
    while j >= 1:
        if z[j - 1] >= z[j]:
            break
        temp = (cc + c[j - 1]) * z[j - 1]
        minn = min(temp, minn)
        cc += c[j - 1]
        j -= 1
    ans.append(minn)
ans = [str(a) for a in ans]
print(" ".join(ans))