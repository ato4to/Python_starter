def checkFunc():

    string_to_check = input("Enter the phrase :")

    if string_to_check == string_to_check[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

checkFunc()