
def main():


    try:
        user_input = input("Enter the numbers youd like to use for the pattern: ")

        with open("pixel_pattern.txt", "w") as file:
            file.write(user_input)


        with open("pixel_pattern.txt", "r") as file:
                  line = file.readline()
                  pattern = line.strip().split(",")
                  pattern = [int(x) for x in pattern]
                  print(pattern)

    except IOError:
        print("Error, please try again")

if __name__ == "__main__":
    main()
