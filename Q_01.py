# CS-500L/Lab-02/Q-01
# 20099_Maniruzzaman_Md_Lab_02
# Q: Write a Python program to implement a simple calculator.....

def main():
# Print the program Title
    print("===== A Simple calculator =====")

    while True:
        first_num = int(input("Enter the first number\t: "))
        second_num = int(input("Enter the second number\t: "))
        operator = input("Enter the operator\t: ")

        result = None
        error_message = None
        if operator == "+":
            result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "*":
            result = first_num * second_num
        elif operator == "/":
            if second_num == 0:
                error_message = "Error, divide by zero!"
            else:
                result = first_num / second_num
        else:
            error_message = "Error, invalid operator!"
        
        if error_message is None:
            print("\nThe result \t\t:", result)
        else:
            print(error_message)
        
        confirm = input("\nDo you want to try again (y/n)")
        if confirm.lower() !="y":
            break
if __name__ == "__main__":
    main()

