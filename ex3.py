def main():
    list = []
    num = int(input("Enter a list of numbers: "))
    list.append(num)

    while (num > 0):
        num = int(input("Enter a list of numbers: "))
        list.append(num)

        if(num == 0):
            list.remove(num)
            break

    if(list[0] == list[-1]):
        print(f"True")
    else:
        print(f"False")
if __name__ == "__main__":
    main()