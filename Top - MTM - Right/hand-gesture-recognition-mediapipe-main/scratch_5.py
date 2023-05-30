import pandas as pd

# Load CSV file into a Pandas DataFrame
df = pd.read_csv('output.csv')

# Create a new column that indicates when a value changes from the previous row
df['value_changed'] = (df['Time (s)'] != df['Time (s)'].shift())

# Create a new column that assigns a unique group ID to contiguous runs of the same value
df['group_id'] = df['value_changed'].cumsum()

# Create a new column that contains the value to subtract at the last occurrence of each group
df['last_value_to_subtract'] = df.groupby('group_id')['Output'].transform('last')

# Create a new column that contains the row above the first occurrence of each group
df['prev_row'] = df['Output'].shift().where(df['value_changed'], None)

# Create a new column that contains the value to subtract at the first occurrence of each group
df['first_value_to_subtract'] = df.groupby('group_id')['prev_row'].transform('last')

# Calculate the difference between the first and last value to subtract for each group
df['difference'] = df['last_value_to_subtract'] - df['first_value_to_subtract']

# Group the DataFrame by group_id and concatenate the values in each group into a comma-separated string
grouped_df = df.groupby('group_id').agg({'Time (s)': 'first', 'difference': 'first'}).reset_index()

# Save the grouped data to a new CSV file
grouped_df.to_csv('grouped_file.csv', index=False)