# CS-500L/Lab-02/Q-05
# 20099_Maniruzzaman_Md_Lab_02
# Q: Draw a rectangle by input data (Height & Width) and symbol......

print("====== Rectangle with Symbols ======")

def rect_of_symbols(height, width, symbol):
    for i in range(height):
        line = symbol * width
        print(line)

def main(): 
    height = int(input("Enter the rectangle's height\t: "))
    width = int(input("Enter the rectangle's width\t: "))
    symbol = input("Enter the symbol\t\t: ")

    if len(symbol) != 1:
        print("Invalid input symbol. Please enter a single character.")
        return
    print("\n")
    rect_of_symbols(height, width, symbol)

if __name__ == "__main__":
    main()

