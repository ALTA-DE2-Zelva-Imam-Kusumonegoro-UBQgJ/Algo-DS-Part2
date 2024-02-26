def maximum_buy_product(money, product_price):
    product_price.sort()
    total_product = 0
    expense = 0
    for i in product_price:
        if expense + i <= money:
            expense += i
            total_product += 1
        else:
            break
    return total_product

if __name__ == "__main__":
    print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))      # 3
    print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000])) # 4
    print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))   # 4
    print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))           # 1
    print(maximum_buy_product(0, [10000, 30000]))                        # 0