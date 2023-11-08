def main():
        
    condition = True
    while condition == True:
        num1 = input("Enter first integer: ")
        if num1 == "exit":
            condition = False
            break
            print("done")
        else:
            num2 = input("Enter second integer: ")
            sum = int(num1) + int(num2)
            print(f"Answer: {sum}")

if __name__ == "__main__":
    main()