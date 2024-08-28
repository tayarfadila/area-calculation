def calculate_area(width, height):
    return width * height

def main():
    print("Welcome to the Rectangle Area Calculator!")
    
    # Get user input for width and height
    try:
        width = float(input("Please enter the width of the rectangle: "))
        height = float(input("Please enter the height of the rectangle: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Calculate the area
    area = calculate_area(width, height)
    
    # Display the result
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()
