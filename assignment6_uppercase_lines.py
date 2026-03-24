# Take multiple lines input and print all lines in uppercase

def uppercase_lines():
    print("Enter lines (type 'end' to stop):")

    lines = []
    while True:
        line = input()
        if line.lower() == "end":
            break
        lines.append(line)

    print("\nUppercase Output:")
    for line in lines:
        print(line.upper())

if __name__ == "__main__":
    uppercase_lines()
