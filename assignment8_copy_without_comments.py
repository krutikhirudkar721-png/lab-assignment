# Copy python file content without comments and print both files

def remove_comments_and_copy():
    src = input("Enter source python file: ")
    dest = input("Enter destination file: ")

    with open(src, 'r') as f:
        lines = f.readlines()

    # Remove comment lines
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("#") and stripped != "":
            new_lines.append(line)

    with open(dest, 'w') as f:
        f.writelines(new_lines)

    # Print both files
    print("\n--- Source File Content ---")
    with open(src, 'r') as f:
        print(f.read())

    print("\n--- Destination File Content (No Comments) ---")
    with open(dest, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    remove_comments_and_copy()
