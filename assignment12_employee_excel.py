# Read employee.xlsx and perform:
# employees in Automotive, search by ID, list developers

import pandas as pd

def employee_analysis():
    df = pd.read_excel("employee.xlsx")

    print("\n--- All Employees ---")
    print(df)

    # a) Employees in Automotive domain
    print("\nEmployees in Automotive:")
    print(df[df['Department'] == "Automotive"])

    # b) Search employee by ID
    emp_id = int(input("\nEnter Employee ID: "))
    print("\nEmployee Details:")
    print(df[df['Employee ID'] == emp_id])

    # c) List of Developers
    print("\nDevelopers:")
    print(df[df['Designation'] == "Developer"])

if __name__ == "__main__":
    employee_analysis()
