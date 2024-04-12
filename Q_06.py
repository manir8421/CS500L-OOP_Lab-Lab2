# CS-500L/Lab-02/Q-06
# 20099_Maniruzzaman_Md_Lab_02
# Q: Draw a triangle by input data and symbol......

print("====== Triangle with Symbols ======")

def tri_of_symbols(height, symbol):
    for i in range(1, height + 1):
        spac = " " * (height - i)
        line = spac + symbol * (2 * i - 1)
        print(line)

def main():
    height = int(input("Enter the height of the triangle\t: "))
    symbol = input("Enter the symbol to use\t\t\t: ")

    if len(symbol) != 1:
        print("Invalid symbol. Please enter a single character.")
        return
    print("\n")
    tri_of_symbols(height, symbol)

if __name__ == "__main__":
    main()

