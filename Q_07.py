# CS-500L/Lab-02/Q-07
# 20099_Maniruzzaman_Md_Lab_02
# Q: Draw a circle by an input alphabet/number........

def is_pos_in_circle(x, y, rad):
    return x * x + y * y <= rad * rad

def draw_circle(radius, symbol):
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if is_pos_in_circle(x, y, radius):
                print(symbol, end=" ")
            else:
                print(" ", end=" ")
        print()  # Add a newline after each row

def main():
    print("===== Print a Circle =====")
    radius = int(input("Please enter the radius of the circle\t: "))
    symbol = input("Please enter the symbol character\t: ")
    print("\n")
    draw_circle(radius, symbol)

if __name__ == "__main__":
    main()
