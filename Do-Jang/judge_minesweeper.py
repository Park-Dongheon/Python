row, col = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
    
for i in range(row):
    for j in range(col):
        count = 0
        if matrix[i][j] == '*':
            print('*', end='')
            continue

        # 위 3칸 탐색
        if i-1 >= 0:
            if matrix[i-1][j] == '*':
                count += 1
            if j > 0:
                if matrix[i-1][j-1] == '*':
                    count += 1
            if j < col-1:
                if matrix[i-1][j+1] == '*':
                    count += 1

        # 아래 3칸 탐색
        if i < row-1:
            if matrix[i+1][j] == '*':
                count += 1
            if j > 0:
                if matrix[i+1][j-1] == '*':
                    count += 1
            if j < col-1:
                if matrix[i+1][j+1] == '*':
                    count += 1

        # 좌우 탐
        if j-1 >= 0:
            if matrix[i][j-1] == '*':
                count += 1
        if j < col-1:
            if matrix[i][j+1] == '*':
                count += 1

        print(count, end='')
        
    print()
