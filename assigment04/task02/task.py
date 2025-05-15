# Step 1: Take user input and write to file
first_input = input("Enter  text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(first_input + "\n")
    print("Data successfully written to the output.txt ")

# Step 2: Take additional input and append to file
second_input = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(second_input + "\n")
    print("Data successfully append")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
