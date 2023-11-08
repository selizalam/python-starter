def main():
    num = input("Enter a number: ")
    
    try:
        num = int(num)
        print(num * -1)
    except ValueError:
        print(f"ERROR: {num} is not an integer.")

if __name__ == "__main__":
    main()