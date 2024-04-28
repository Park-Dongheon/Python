paragraph = input()
words = paragraph.split()
count = 0
for i in words:
    if i.strip(',.') == 'the':
        count += 1 
print(count)
