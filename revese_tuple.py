#Reverse the tuple

t = eval(input("Enter numbers seprated by comma: "))
print("User entered tuple is ",t)
l = list(t)
l.reverse()
t = tuple(l)

print("Reverse of tuple is",t)