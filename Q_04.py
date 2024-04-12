# CS-500L/Lab-02/Q-04
# 20099_Maniruzzaman_Md_Lab_02
# Q: Time shift after and befor the enter time........

def main():
    print("Find the time X minutes before and after the input time")
    cur_time = input("Enter a time (hh:mm)\t\t: ")
    cur_hours = int(cur_time.split(":")[0])
    cur_mins = int(cur_time.split(":")[1])

    shift_mins = int(input("Enter a time shift in mins\t: "))

    total_cur_mins = cur_hours * 60 + cur_mins

    # Calculate the time after x minutes
    total_after_mins = total_cur_mins + shift_mins
    after_hours = (total_after_mins // 60) % 24
    after_mins = total_after_mins % 60
    print(f"After time is\t\t\t: {after_hours:02d}:{after_mins:02d}")

    # Calculate the time before x minutes
    total_before_mins = total_cur_mins - shift_mins
    before_hours = (total_before_mins // 60) % 24
    before_mins = total_before_mins % 60
    print(f"Before time is\t\t\t: {before_hours:02d}:{before_mins:02d}")

if __name__ == "__main__":
    main()


