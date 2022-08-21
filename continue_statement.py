"""
Write a program to print all numbers between two intervals, namely low and high.
 But, with a special condition that numbers divisible by 5 must not be printed and skipped.
  (Do this using continue Statement)
"""
 
low, high = input("Enter two numbers: ").split()

for i in range(int(low), int(high) + 1):
    if i%5 == 0:
        continue
    print(i, end = " ") 

    