#!/usr/bin/python3

# Define a fucion to read and print the content of a file
def read_file(filename=""):
    # Open the file in read mode
    with open(filename, 'r', encoding="utf-8") as file:
        # Read and print each line
        for line in file:
            print(line, end='')
