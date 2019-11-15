class Counter:
    def __init__(self,low,high):
        self.low = low
        self.high = high
        # print(self.low,self.high)

    def __iter__(self):
        # print(self.low,self.high)
        return self

    def __next__(self):
        if self.low<self.high:
            num = self.low
            self.low+=1
            return num
        else:
            raise StopIteration


for n in Counter(50,55):
    print(n)
