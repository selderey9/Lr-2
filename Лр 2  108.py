km_per_hour=int(input("Enter your speed km/h (Only intergers allowed):"))
meters_per_second=int(input("Enter your speed in m/s (Only intergers allowed):"))
converted_meters_per_second=meters_per_second*3.6
if converted_meters_per_second > km_per_hour:
    print(meters_per_second, "is faster")