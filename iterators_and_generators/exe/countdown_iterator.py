class countdown_iterator:

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration

        current_num = self.start
        self.start -= 1
        return current_num


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")