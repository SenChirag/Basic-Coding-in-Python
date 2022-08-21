first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if(first == second == third):
    print("All numbers are equal")
elif(first == second):
    if(first > third):
        print(str(first)," is greatest")
    else:
        print(str(third), " is greatest")
elif(first == third):
    if(first > second):
        print(str(first), " is greatest")
    else:
        print(str(third), "is greatest")
elif(second == third):
    if(second > first):
        print(str(second), " is greatest")
    else:
        print(str(third(), " is greatest"))
elif(first > (second and third)):
    print(str(first ), " is greatest")
elif(second > (first and third)):
    print(str(second), " is greatest")
else:
    print(str(third), " is greatest")