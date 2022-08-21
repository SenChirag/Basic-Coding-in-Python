first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if(first == second):
    print("Both numbers are equal")
elif(first > second):
    print(str(first)," is greater than ", str(second))
else:
    print(str(second), " is greater than ", str(first) )