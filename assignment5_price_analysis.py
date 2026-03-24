# Store item prices in tuple and perform:
# count items, cheapest, costliest, sort, count max price items

def price_analysis():
    prices = tuple(map(int, input("Enter item prices: ").split()))

    print("\nPrices:", prices)

    # a) Total items
    print("Total items sold:", len(prices))

    # b) Cheapest item
    print("Cheapest price:", min(prices))

    # c) Costliest item
    print("Costliest price:", max(prices))

    # d) Ascending order
    print("Sorted prices:", tuple(sorted(prices)))

    # e) Count of costliest items
    max_price = max(prices)
    print("Number of costliest items:", prices.count(max_price))

if __name__ == "__main__":
    price_analysis()
