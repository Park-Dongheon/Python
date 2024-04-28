height = int(input())

for i in range(height):

    for j in range(height):
        if j < i:
            print('*', end='')
    print()
