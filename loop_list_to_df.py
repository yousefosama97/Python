# Import the Pandas library
import pandas as pd

# Define the function 'populate_dataframe' that takes a list 'data_list' as input
def populate_dataframe(data_list):
    # Check if the length of 'data_list' is not a multiple of 4
    if len(data_list) % 4 != 0:
        # If it's not a multiple of 4, raise a ValueError with an appropriate error message
        raise ValueError(f"The length of the list should be a multiple of 4., currently the list has {len(data_list)} person")
    
    # Calculate the number of rows needed for the DataFrame, assuming each row contains 4 elements
    num_rows = len(data_list) // 4
# looping a list to append to dataframe
# Given a list lname containing elements representing people's names in groups of four. the function to convert this list into a DataFrame.
  
    # Create an empty DataFrame with columns 'A', 'B', 'C', and 'D'
    df = pd.DataFrame(columns=['A', 'B', 'C', 'D'])
    
    # Loop through the calculated number of rows
    for i in range(num_rows):
        # Calculate the start index of the slice for the current row
        start_index = i * 4
        
        # Calculate the end index of the slice for the current row
        end_index = (i + 1) * 4
        
        # Extract a slice of 4 elements from 'data_list' for the current row
        row_data = data_list[start_index:end_index]
        
        # Assign the extracted row_data to the 'i'-th row in the DataFrame
        df.loc[i] = row_data

    # Return the populated DataFrame
    return df

# Input list
lname = ['A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D']

# Call the 'populate_dataframe' function with the input list and print the resulting DataFrame
try:
    result_df = populate_dataframe(lname)
    print(result_df)
except ValueError as e:
    print(e)
