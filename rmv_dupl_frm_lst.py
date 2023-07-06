names = []

n = int(input("How many numbers do you want to enter? :  "))

for i in range(n):
    print(i+1, "Enter name: ")
    names.append(input())

print("\n")
s = set(names)
names = list(s)
for x in names:
    print(x)
