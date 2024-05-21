"""
Method for printing the reversed pyramid shape based on for-loop
"""
def reversed_pyramid(size):

    for i in range(size, 0, - 1):  # Loop through each row in reverse order
            stars = "*" * i  # Calculate the number of stars for each row
            print(stars)

