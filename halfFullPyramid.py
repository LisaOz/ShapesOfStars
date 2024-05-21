"""
Method for displaying a half pyramid shape of stars based on for-loop
"""
def half_full_pyramid(size):
    for i in range(1, size + 1):  # Loop through each row, adding one star to each row
        stars = ("*" * i) # Calculate the number of stars for each row
        print(stars)

