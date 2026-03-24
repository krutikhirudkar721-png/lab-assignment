# Read a file and write its content in uppercase to another file

def uppercase_file():
    src = input("Enter source file name: ")
    dest = input("Enter destination file name: ")

    with open(src, 'r') as f:
        content = f.read()

    with open(dest, 'w') as f:
        f.write(content.upper())

    print("\nContent copied in uppercase successfully!")

if __name__ == "__main__":
    uppercase_file()
