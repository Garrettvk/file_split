# Pandas is an open source library that is used to analyze data in Python.
import pandas as pd

duplicates = [] # list for duplicate product names
unique = [] # list for unique product names

df = pd.read_csv('output.csv') # df = the csv file we want to read

# productname_df = a dataframe containing tuples of each row in df (index, productname)
productname_df = df[['productname']]

# tuples containing (index, true/false) for each name in productname_df
duplicate_names = productname_df.duplicated(keep=False).iteritems()

# for each name and index in duplicate_names
for index, name in enumerate(duplicate_names):
    
    isduplicate = name[1] # index 1 of name tells us if its a duplicate (index, true/false)   
    
    csv_row = df.loc[index] # current csv row from original file

    # if the name is a duplicate
    if isduplicate:        
        duplicates.append(csv_row) # add the product name to duplicates list

    else:        
        unique.append(csv_row) # add product name to unique list

# default columns for the DataFrames
default_columns = ['productname', 'category1', 'category2', 'category3', 'image1', 'image2', 'description', 'price']

# DataFrame for duplicates
duplicate_df = pd.DataFrame(
    duplicates, # the list we're using for data
    columns=default_columns # columns for DataFrame 
    )

# DataFrame for unique product names
unique_df = pd.DataFrame(
    unique, # the list we're using for data
    columns=default_columns # columns for DataFrame
    )

# write DataFrames to individual csv files
duplicate_df.to_csv('duplicates.csv', mode='w', index=False)
unique_df.to_csv('unique.csv', mode='w', index=False)