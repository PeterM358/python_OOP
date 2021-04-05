def number_increment(numbers):
    def increase():
        nums = [el + 1 for el in numbers]
        return nums
    return increase()


print(number_increment([1, 2, 3]))