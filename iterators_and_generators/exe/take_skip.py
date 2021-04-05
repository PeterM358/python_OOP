class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.initial = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration
        current_step = self.initial
        self.initial += self.step
        self.counter += 1
        return current_step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


