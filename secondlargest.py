# Program to find the second largest number in a list

numbers = [10, 25, 7, 42, 18, 35]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second largest number:", unique_numbers[-2])