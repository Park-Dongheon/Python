a = {i for i in range(1, 101) if i % 3 == 0}
b = {j for j in range(1, 101) if j % 5 == 0}

print(a & b)
