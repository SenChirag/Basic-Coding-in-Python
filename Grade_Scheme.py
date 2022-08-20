marks = int(input("Enter your marks out of 100 : "))

if(marks < 0 or marks > 100):
    print("invalid")
elif(marks < 30):
    print("Fail")
elif(marks < 50):
    print("Grade D")
elif(marks < 60):
    print("Grade C")
elif(marks < 70):
    print("Grade B")
elif(marks < 80):
    print("Grade A")
else:
    print("Grade A+")