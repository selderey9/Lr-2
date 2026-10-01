while True:  # cycle in case of error
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    s = int(input("Enter sum:"))
    if a >= b or b >= c or a >= c:  # checking if there is no logical errors
        print("Error, try again!")
    else:
        if s <= a:
            print("Your tax is:", s * 0)
        elif a < s <= b:
            print("Your tax is:", s * 0.1)
        elif a < s <= c and s > b:
            print("Your tax is:", s * 0.25)
        elif s > a and s > b and s > c:
            print("Your tax is", s * 0.5)
        break  # breaking the cycle in case errors haven`t occur
