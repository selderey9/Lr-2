while True:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter third number:"))
    if a == b or b == c or c == a:
        print("Numbers can`t be equal. Try again!")
    else:
        if a > b:
            if a > c:
                print("Result:", b * c)
            elif c > a:
                print("Result:", a * b)
        elif b < c:
            print("Result:", b * a)
        else:
            print("Result:", c * a)
        break
