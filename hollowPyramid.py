"""
Method to print the hollow pyramid shape using for-loop
"""
def hollow_pyramid(size):
    for i in range(size):  # Loop through each row, excluding the base row
        spaces = " " * (size - i - 1)  # Calculate the number of spaces before the stars
        if i == 0 or i == size:  # First or last row
            stars = "*" * (2 * i + 1)
        else:
            stars = "*" + " " * (2 * i - 1) + "*"  # Hollow part of the triangle
        print(spaces + stars)

