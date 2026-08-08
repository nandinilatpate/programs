import pandas as pd

# Create a DataFrame from a dictionary of lists
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 28, 22],
    "Marks": [85, 90, 78, 88, 95],
    "City": ["New York", "London", "Paris", "Tokyo", "Sydney"]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Select a single column
print("\nSelect 'Name' column:")
print(df["Name"])

# Select multiple columns
print("\nSelect 'Name' and 'Marks' columns:")
print(df[["Name", "Marks"]])

# Select the first row
print("\nFirst Row:")
print(df.iloc[0])

# Select the first three rows
print("\nFirst Three Rows:")
print(df.iloc[0:3])

# Filter rows where Marks are greater than 85
print("\nStudents with Marks greater than 85:")
print(df[df["Marks"] > 85])

# Filter rows where Age is less than 30
print("\nStudents with Age less than 30:")
print(df[df["Age"] < 30])

# Sort the DataFrame by Age (Ascending)
print("\nSorted by Age (Ascending):")
print(df.sort_values(by="Age"))

# Sort the DataFrame by Marks (Descending)
print("\nSorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))