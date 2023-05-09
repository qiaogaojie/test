import sys
n = int(input())
line = sys.stdin.readline().strip()
line = list(map(int, line.split()))
line = sorted(line)
ans = 0
for i in range(n - 1):
  ans += line[i + 1] - line[i]
print(ans)