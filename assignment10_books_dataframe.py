# Read books.csv using pandas and perform:
# display all, filter by author/publisher, find cheapest & costliest, sort by year

import pandas as pd

def books_operations():
    df = pd.read_csv("books.csv")

    # a) Complete report
    print("\n--- All Books ---")
    print(df)

    # b) Books by author
    author = input("\nEnter author name: ")
    print("\nBooks by author:")
    print(df[df['author'] == author])

    # c) Books by publisher
    publisher = input("\nEnter publisher name: ")
    print("\nBooks by publisher:")
    print(df[df['publisher'] == publisher])

    # d) Cheapest & costliest books
    cheapest = df[df['price'] == df['price'].min()]
    costliest = df[df['price'] == df['price'].max()]
    print("\nCheapest Book Titles:")
    print(cheapest['title'])
    print("\nCostliest Book Titles:")
    print(costliest['title'])

    # e) Sort by year
    print("\nBooks sorted by publication year:")
    print(df.sort_values(by='year'))

if __name__ == "__main__":
    books_operations()
