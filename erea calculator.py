print("Rushaid's Land Area/Volume Calculator!")
while True:
# Ask if height is included
    while True:
        print(f"--------------------------------------------------------------------------------------")
        include_height = input(f"would you like to include the height of the land? (yes/no): ").lower()
        if include_height in ['yes', 'no']:
            break
        print("please type yes or no only")

# lenghth and width or height 
    while True:
        try:
            print(f"--------------------------------------------------------------------------------------")
            length = float(input(f"enter the length of your land (meters): "))
            width = float(input(f"enter the width of your land (meters): "))
            if length <= 0 or width <= 0:
                print(f"--------------------------------------------------------------------------------------")
                print(f"length and width must be positive numbers.")
                continue
            break
        except ValueError:
            print(f"--------------------------------------------------------------------------------------")
            print(f"invalid numbers.")

    if include_height == 'yes':
        while True:
            try:
                height = float(input(f"enter the height of your land (meters): "))
                if height <= 0:
                    print(f"--------------------------------------------------------------------------------------")
                    print(f"height must be a positive number.")
                    continue
                break
            except ValueError:
                print(f"--------------------------------------------------------------------------------------")
                print(f"please enter a valid number.")

        area = length * width * height
        print(f"--------------------------------------------------------------------------------------")
        print(f"\nyour land volume is {area} cubic meters.\n")
    else:
        area = length * width
        print(f"--------------------------------------------------------------------------------------")
        print(f"\nyour land area is {area} square meters.\n")

# if wanna close the program
    while True:
        print(f"--------------------------------------------------------------------------------------")
        close = input(f"would you like to close the program? (yes/no): ").lower()
        if close == 'yes':
            print(f"goodbye!")
            exit()
        elif close == 'no':
            print(f"lets continue!\n")
            break
        else:
            print(f"please type yes or no")
            