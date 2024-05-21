from halfFullPyramid import half_full_pyramid
from hollowPyramid import hollow_pyramid
from reversedPyramid import reversed_pyramid
def main():
    # Main program loop with displaying a pattern for choices
    while True:
        print("..........................................")
        print(":                                        :")
        print(":      -*- Choose the option -*-         :")
        print(":  1. Hollow Empty Pyramid               :")
        print(":  2. Half Full Pyramid                  :")
        print(":  3. Reversed Half Full Pyramid         :")
        print(":                                        :")
        print("..........................................")

        # Prompt user for the choice of the shape
        choice = input("Enter the choice or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Quitting the program")
            break

        # Prompt user for the size of the shape
        try:
            size = int(input("Enter the size: "))
        except ValueError:
            print("Invalid input, please enter a positive number")
            continue # continue to the next  iteration

        if choice == "1":
            hollow_pyramid(size)

        elif choice == "2":
            half_full_pyramid(size)

        elif choice == "3":
            reversed_pyramid(size)

        else:
            print("Incorrect choice")

if __name__ == "__main__":
    main()
