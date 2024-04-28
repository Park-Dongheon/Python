with open('words.txt', 'r') as file:
    for line in file:
        words = line.strip().split()    # 각 줄을 공백으로 나누어 단어를 추출
        for word in words:
            word = word.strip(',.')     # 단어에서 콤마와 점을 제거
            if 'c' in word:
                print(f'{word}')
