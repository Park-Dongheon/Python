height = int(input())

for i in range(height):
    for j in range(height):
        if j+i < (height-1)-i:
            print(' ', end='')
        else:
            print('*', end='')
    height += 1
    print()
