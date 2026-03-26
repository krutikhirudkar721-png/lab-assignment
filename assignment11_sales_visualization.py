# Analyze cosmetic sales data using matplotlib:
# line plot (profit), multiline plot (products), bar chart (facewash/cream), pie chart (yearly sales)

import pandas as pd
import matplotlib.pyplot as plt

def sales_analysis():
    df = pd.read_csv("sales_data.csv")

    # a) Line plot - total profit
    plt.figure()
    plt.plot(df['month'], df['total_profit'])
    plt.title("Total Profit per Month")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.show()

    # b) Multiline plot - product sales
    plt.figure()
    plt.plot(df['month'], df['facecream'], label="Face Cream")
    plt.plot(df['month'], df['facewash'], label="Face Wash")
    plt.plot(df['month'], df['toothpaste'], label="Toothpaste")
    plt.legend()
    plt.title("Product Sales Data")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.show()

    # c) Bar chart - facecream & facewash
    plt.figure()
    plt.bar(df['month'], df['facecream'], label="Face Cream")
    plt.bar(df['month'], df['facewash'], bottom=df['facecream'], label="Face Wash")
    plt.legend()
    plt.title("Face Cream & Face Wash Sales")
    plt.show()

    # d) Pie chart - total yearly sales
    total_sales = [
        df['facecream'].sum(),
        df['facewash'].sum(),
        df['toothpaste'].sum()
    ]

    labels = ["Face Cream", "Face Wash", "Toothpaste"]

    plt.figure()
    plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
    plt.title("Yearly Sales Distribution")
    plt.show()

if __name__ == "__main__":
    sales_analysis()
