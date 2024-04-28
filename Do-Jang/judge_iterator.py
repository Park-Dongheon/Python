class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __getitem__(self, index):
        if index < 0 or index >= (self.stop - self. start):
            raise IndexError

        current = self.start + index
        hours = current // 3600 % 24
        minutes = current // 60 % 60
        seconds = current % 60

        time_str = '{0:02d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds)

        return time_str
        
start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
