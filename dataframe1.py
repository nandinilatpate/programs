import pandas as pd

# Dictionary of lists
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)