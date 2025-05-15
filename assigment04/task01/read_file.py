try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line, end="")  # end="" to avoid double newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
