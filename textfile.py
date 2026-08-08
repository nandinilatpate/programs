# Program to count the number of words in a text file

with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()

print("Number of words:", len(words))