print(" Simple Calculator")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\nSelect Operation")
print("1: Addition (+)")
print("2:Subtraction (-)")
print("3: Multiplication (*)")
print("4: Division (/)")

choice = input("\nEnter Choice (1-4): ")

if choice == "1":
    result = num1 + num2
    print("\nResult =", result)

elif choice == "2":
    result = num1 - num2
    print("\nResult =", result)

elif choice == "3":
    result = num1 * num2
    print("\nResult =", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("\nResult =", result)
    else:
        print("\nError! Division by zero is not allowed.")

else:
    print("\nInvalid Choice!")