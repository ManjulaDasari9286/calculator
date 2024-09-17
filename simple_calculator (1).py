def simple_calculator():
    n1= float(input("Enter the first number : "))
    n2=float(input("Enter the second number : "))
    print("Choose the opertion from below\n '+' for addition \n '-' for subtraction \n '*' for multiplication \n '/' for divison")
    choice =input(" Enter your choice('+' or '-' or '*' or '/')")
    if choice == '+':
        print(n1,"+",n2,"=",n1+n2)
    elif choice== '-':
        print(n1,"-",n2,"=",n1-n2)
    elif choice == "*":
        print(n1,"*",n2,"=",n1*n2)
    elif choice == "/":
        if n2 !=0:
            print(n1,"/",n2,"=",n1/n2)
        else:
            print("Zero divison error!")
    else:
        print("Invalid choice! try again")
simple_calculator()