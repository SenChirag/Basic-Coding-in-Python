# Write a python script to print indices of all occurrence of a given element in a given list

l = [eval(x) for x in input("Enter list elements: ").split(',')]
element = input("Enter element value: ")
index = 0
while index<len(l):
    if l[index]==element:
        print(index,end=' ')
print(l)
