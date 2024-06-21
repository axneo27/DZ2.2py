a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a==b:
    print("Numbers are equal")
else:
    if a>b:
        print(f"{b}, {a}")
    else:
        print(f"{a}, {b}")