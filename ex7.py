import random

def main():
    list = []
    randNum = random.randint(0,100)

    if randNum < 10:
        print(f"{randNum}: You lose.")
    elif randNum > 10 and randNum < 50:
        print(f"{randNum}: Try again.")
    else:
        print(f"{randNum}: You win!")

if __name__ == "__main__":
    main()