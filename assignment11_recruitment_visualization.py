# Visualize recruitment data using bar, pie, customized pie, doughnut and compare companies

import matplotlib.pyplot as plt

def recruitment_analysis():
    companies = ["Microsoft", "Google", "Amazon", "IBM", "Amdocs"]
    hires = [120, 150, 180, 100, 90]

    # a) Bar chart
    plt.figure()
    plt.bar(companies, hires)
    plt.title("Recruitment by Company")
    plt.show()

    # b) Pie chart
    plt.figure()
    plt.pie(hires, labels=companies, autopct='%1.1f%%')
    plt.title("Recruitment Distribution")
    plt.show()

    # c) Customized pie chart
    plt.figure()
    plt.pie(hires, labels=companies, autopct='%1.1f%%', explode=[0,0.1,0,0,0])
    plt.title("Customized Pie Chart")
    plt.show()

    # d) Doughnut chart
    plt.figure()
    plt.pie(hires, labels=companies, autopct='%1.1f%%')
    centre_circle = plt.Circle((0,0),0.70)
    plt.gca().add_artist(centre_circle)
    plt.title("Doughnut Chart")
    plt.show()

    # e) Compare IBM & Amdocs
    plt.figure()
    compare_companies = ["IBM", "Amdocs"]
    compare_values = [100, 90]
    plt.bar(compare_companies, compare_values)
    plt.title("IBM vs Amdocs Recruitment")
    plt.show()

if __name__ == "__main__":
    recruitment_analysis()
