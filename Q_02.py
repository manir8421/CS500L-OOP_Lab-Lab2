# CS-500L/Lab-02/Q-02
# 20099_Maniruzzaman_Md_Lab_02
# Q: Write a Python program CD value, APY, CD term, Compounding frequency ......

def main():                                                         # main function declear for all input data
    investment = float(input("Enter initial investment amount\t\t\t\t\t: "))
    annual_yield = float(input("Enter annual percentage yield (APY)\t\t\t\t: "))
    months = int(input("Enter number of months for CD term\t\t\t\t: "))
    compounding = input("Enter compounding frequency (monthly, quarterly, annually)\t: ")
    if check_compounding(months, compounding):                      #Variable forward to "check_compounding" function
        compounding = check_compounding(months, compounding)
        calc(investment, annual_yield, months, compounding)         #variable forward to "calc" function for calculation

def check_compounding(months, compounding):                         #check_com function declear and receive variable from previous function 
    if months%12 == 0:
        if compounding == "quarterly":
            return 3
        if compounding == "annually":
            return 12
    if months%4 == 0:
        if compounding == "quarterly":
            return 3
    if compounding == "monthly":
        return 1
    print("Invalid Compounding frequency")

def calc(investment, annual_yield, months, compounding):            # receive variable from previous function
    arr = []                                                        # [[1, 5014.58], [2, 5029.21]] result store type array in array
    interest = 0
    for i in range(1, int(months//compounding) + 1):                # i is the number of row according compounding
        value = (investment * annual_yield * compounding) / (12 * 100)
        interest += value
        investment += value
        arr.append([i, investment])
    display(arr, interest, compounding)                             # forward variable to function display

def display(arr, interest, compounding):                            # display function receive the variablr from calc function
    if compounding == 3:
        header = "Quarter"
    if compounding == 12:
        header = "Year"
    if compounding == 1:
        header = "Month"
    print("\n")
    print(f"{header}\t\t CD Value\n------\t\t --------")            # Hearder print
    for i in arr:
        print("{}\t\t {:.2f}".format(i[0], i[1]))                   # Output value print from array
    print("\nTotal interest earned: $", format(interest, ".2f"))    # Error print for invalid data input

if __name__ == "__main__":
    main()