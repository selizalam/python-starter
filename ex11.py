def main():
    file = open("output.txt", "w")
    file.write("08/17/2021")
    file.close()

    file = open("output.txt", "r")
    print(f"Today's date is: " + file.read())
    
if __name__ == "__main__":
    main()