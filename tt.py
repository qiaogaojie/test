import sys
while True:
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    if line:
        print(line)
    else:
        break
l = ['234', 'dk']
print(" ".join(l))