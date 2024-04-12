# CS-500L/Lab-02/Q-03
# 20099_Maniruzzaman_Md_Lab_02
# Q: Print the word according to input order and shorted list then not repet and in alphabetic serial....

def main():
    print("========== A list of words ==========")

    """
    task 1
    """

    list_of_words = []
    word = input("Enter a word: ")
    while word.lower() != "exit":
        list_of_words.append(word)
        word = input("Enter a word: ")
    
    print ("The original list: ")
    print(list_of_words)

    sorted_list = sorted(list_of_words)
    print("The sorted list: ")
    print(sorted_list)

    """
    task 2
    """

    print("The unique words: ")
    for i in range(len(list_of_words)):
        print_yes = True
        for j in range(0,i):
            if list_of_words[i] == list_of_words[j]:
                print_yes = False
        if print_yes:
            print(list_of_words[i], end=",")


if __name__ == "__main__":
    main()