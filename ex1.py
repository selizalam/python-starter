import random

def main():
    sum = 0
    list = []
    randNum = random.randint(0,100)

    for x in range(0, 10):
        list.append(randNum)
        sum += list[x]
    print(f"sum is {sum}")

if __name__ == "__main__":
    main()