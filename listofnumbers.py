# Function to find the largest number in a list

def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers = [10, 25, 7, 42, 18]

print("Largest number:", find_largest(numbers))