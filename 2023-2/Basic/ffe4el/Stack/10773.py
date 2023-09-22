import sys


k = int(sys.stdin.readline())

a = []

for _ in range(k):
    n = int(sys.stdin.readline())
    if n != 0:
        a.append(n)
    else:
        a.pop()

total = 0

for i in a:
    total += i

print(total)