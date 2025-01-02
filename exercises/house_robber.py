
def house_robber(houses):
    # [rob1, rob2, n, n+1, ...]
    rob1, rob2 = 0, 0

    for house in houses:
        temp = max(house + rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


print(house_robber([1, 2, 3, 1]))