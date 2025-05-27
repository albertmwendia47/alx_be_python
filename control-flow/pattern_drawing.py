pattern = int(input("Enter the size of the pattern:"))

row = 0
while row < pattern:
    for col in range(pattern):
        print("*", end="")  # Print * without newline
    print()  # Move to next line after each row
    row += 1


    