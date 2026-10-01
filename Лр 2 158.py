number = input("Enter a two digit number:")
number_massive = list(map(int, number))
sum_of_number = number_massive[0] + number_massive[1]
true_or_false = None
if 10 <= sum_of_number <= 99:
    true_or_false = True
else:
    true_or_false = False
print(true_or_false)