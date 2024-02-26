def playing_domino(cards, deck):
    max_value = 0
    for i in cards:
        if i[0] == deck[1] or i[1] == deck[1]:
            if max_value == 0 or max(i) > max(max_value):
                max_value = i
    if max_value != 0:
        return max_value
    else:
        return []

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []