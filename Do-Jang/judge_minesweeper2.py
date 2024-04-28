row, col = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
    
for x in range(row):
    for y in range(col):
        if matrix[x][y] == '*':
            print(matrix[x][y], end='')
        else:
            count = 0
            for xo in range(x-1, x+2):
                for yo in range(y-1, y+2):
                    if xo < 0 or yo < 0 or xo >= row or yo >= col:
                        continue
                    else:
                        count += 1
            print(count, end='')
                
