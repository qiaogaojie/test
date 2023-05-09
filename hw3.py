a = [1, 2, 3]
import collections
b = collections.deque(a)
print(b.popleft())
print(len(b))