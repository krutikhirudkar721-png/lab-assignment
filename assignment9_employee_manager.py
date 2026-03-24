# Create Employee class, inherit Manager, input & display details of 10 managers

class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Address: {self.address}")


class Manager(Employee):
    pass


def manage_employees():
    managers = []

    for i in range(10):
        print(f"\nEnter details for Manager {i+1}:")
        name = input("Name: ")
        age = int(input("Age: "))
        salary = float(input("Salary: "))
        address = input("Address: ")

        manager = Manager(name, age, salary, address)
        managers.append(manager)

    print("\n--- Manager Details ---")
    for m in managers:
        m.display()


if __name__ == "__main__":
    manage_employees()
