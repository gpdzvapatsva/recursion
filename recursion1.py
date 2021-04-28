user_input = int(input("Enter number"))
def fact(num_1):
    if num_1 == 1 or num_1 == 0:
        return 1
    elif num_1 < 0 :
        return "Enter positive number"
    else:
        return num_1 * fact(num_1 - 1) #calls fuction
result = fact(user_input)
print(result)