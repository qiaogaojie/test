import sys
line = sys.stdin.readline().strip()
line = list(map(int, line.split()))
N, M = line[0], line[1]
height = []
for i in range(N):
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    height.append(line)
line = sys.stdin.readline().strip()
line = list(map(int, line.split()))
X, Y, Z, W = line[0], line[1], line[2], line[3]
if height[X][Y] >= height[Z][W]:
    print(0)

else:
    def dfs(x, y):
        if x == Z and y == W:
            s.append(1)
        else:
            for c in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if c[0] >= 0 and c[0] < N and c[1] >= 0 and c[1] < M:
                    if height[c[0]][c[1]] > height[x][y]:

                        dfs(c[0], c[1])

                    elif height[c[0]][c[1]] == height[x][y]:
                        if c[0] == Z and c[1] == W:
                            dfs(c[0], c[1])
                            
                            
    s = []
    dfs(X, Y)
    print(len(s))