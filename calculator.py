num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
op= input("Enter the operator :")
if op=="+":
    print(f"Addition:{num1+num2}")
elif op=="-":
    print(f"Subtraction:{num1-num2}")
elif op=="*":
    print(f"Multipliction:{num1*num2}")
elif op=="/":
    print(f"Division:{num1/num2}")
else:
    print("Invalid operator")