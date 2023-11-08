def main():
    pythonString = input("Enter string: ") 
    stringList = list(pythonString) 
    vowels = 0
    consonants = 0
    for x in stringList:
        if x == "a" or x == "A":
            vowels += 1
        elif x == "e" or x == "E":
            vowels += 1
        elif x == "i" or x == "I":
            vowels += 1
        elif x == "o" or x == "O":
            vowels += 1
        elif x == "u" or x == "U":
            vowels += 1
        else:
            consonants += 1
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")

if __name__ == "__main__":
    main()