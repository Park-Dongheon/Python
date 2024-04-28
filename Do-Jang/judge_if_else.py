Korean, English, Mathematics, Science = map(int, input().split())
Average = (Korean + English + Mathematics + Science) / 4
if 0 <= Korean <= 100 and 0 <= English <= 100 and 0 <= Mathematics <= 100 and 0 <= Science <= 100:
    if Average >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')
