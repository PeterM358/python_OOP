def fibonacci():
    previous_num = 0
    next_num = 1

    while True:
        yield previous_num
        previous_num, next_num = next_num, previous_num + next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))


