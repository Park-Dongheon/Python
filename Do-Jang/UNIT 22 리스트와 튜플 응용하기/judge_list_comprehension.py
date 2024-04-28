start, stop = map(int, input().split())
c = [2**i for i in range(start, stop+1)]
c.pop(1)
c.pop(-2)
print(c)
