# Program to count the frequency of each word in a string

text = input("Enter a string: ")

words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)