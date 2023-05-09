import sys
n = int(input())
line = sys.stdin.readline().strip()
f = list(map(int, line.split()))
line2 = sys.stdin.readline().strip()
gr = list(map(int, line2.split()))
ans = 0
children = {}
for i in range(n - 1):
    if f[i] in children:
        f[i].append(i)
    else:
        f[i] = [i]
def dfs(f, c):
    if f not in children:
        return 
    if gr[f] == 1:
        ans += (sum(children[f]))
    else:
        temp = children[f][0] ^ children[f][1]
        ans += temp
dfs(1, gr[0])
print(ans)