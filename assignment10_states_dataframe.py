# Create dataframe of states and perform:
# display all, largest area/population, density, highest density

import pandas as pd
def states_operations():
    data = {
        "State": ["State1", "State2", "State3", "State4", "State5"],
        "Area": [120000, 95000, 150000, 80000, 110000],
        "Population": [5000000, 7000000, 6000000, 4000000, 6500000]
    }

    df = pd.DataFrame(data)

    # a) Complete info
    print("\n--- State Data ---")
    print(df)

    # b) Largest area
    print("\nState with largest area:")
    print(df.loc[df['Area'].idxmax(), 'State'])

    # c) Largest population
    print("\nState with largest population:")
    print(df.loc[df['Population'].idxmax(), 'State'])

    # d) Population density
    df['Density'] = df['Population'] / df['Area']
    print("\n--- With Density ---")
    print(df)

    # e) Highest density
    print("\nState with highest density:")
    print(df.loc[df['Density'].idxmax(), 'State'])

if __name__ == "__main__":
    states_operations()
