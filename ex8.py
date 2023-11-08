def main():
    myList = [6,2,7,3,77,7,1]
    min_number = myList[0]

    for number in myList:
        if number < min_number:
            min_number = number
    print(f"{min_number}")

if __name__ == "__main__":
    main()