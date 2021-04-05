class Child:
    cost: float = 0  # cost per day

    def __init__(self, food_cost: int, *toys_cost):
        Child.cost = food_cost + sum(t for t in toys_cost)


