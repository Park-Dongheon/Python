start, stop = map(int, input().split())
x = [2 ** i for i in range(start, stop+1)]
x.pop(1)
x.pop(-2)
print(x)
