while True:
    n = int(input("Enter a 4 digit number:"))
    if n > 9999 or n < 1000:
        print("try again")
    else:
        num = list(map(int, str(n)))
        if num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:

            print(False)
        else:
            print(True)

        break
