# Take integer input as tuple and perform:
# count items, last item, reverse, check 5, remove first & last, sort remaining

def tuple_operations():
    nums = tuple(map(int, input("Enter integers separated by space: ").split()))

    print("\nTuple:", nums)

    # a) Total number of items
    print("Total items:", len(nums))

    # b) Last item
    print("Last item:", nums[-1])

    # c) Reverse tuple
    print("Reversed tuple:", nums[::-1])

    # d) Check if 5 exists
    print("Contains 5:", "Yes" if 5 in nums else "No")

    # e) Remove first & last, sort remaining
    if len(nums) > 2:
        new_tuple = tuple(sorted(nums[1:-1]))
        print("Modified tuple:", new_tuple)
    else:
        print("Not enough elements to modify")

if __name__ == "__main__":
    tuple_operations()
