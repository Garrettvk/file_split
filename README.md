the input of the parser needs to be output.csv

This file uses Pandas, inside of Pandas there's a data type called DataFrame. DataFrames are similar to csv files.

df 
    is our main DataFrame which contains everything from out input file. In this case our input file is output.csv

productname_df
    a DataFrame containing tuples of (index, productname). This will help us compare the product names in each row of csv.

duplicate_names
    a DataFrame containing tuples of (index, true/false). The first index of these tuples are used in the for loop to determine if the name is a duplicate or not.

on the for loop I used enumerate because it lets you create a counter/index

    isduplicate 
        a variable that return true or false depednding on the iteration of the loop

    csv_row 
        the current row of the original DataFrame df. We want to keep the entire row as a variable so we can put it inside one of our lists.

    if/else statement
        this checks if the name is a duplicate and then puts the current csv row in the correct list

now that the data is separated into lists we can put the data from the lists into individual DataFrames. Then use "to_csv" to write those DataFrames to csv files.

I feel like it would make more sense to only use DataFrames and throw out the lists but I couldn't figure out how to make that work.