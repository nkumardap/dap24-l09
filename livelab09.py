"""
EXERCISE 1

Short: Open the gdp data and turn it into a CLEAN long-shaped dataframe.
Make sure that the resulting year variable is an int object

Long: Open gdp.csv, and use melt() to convert it into a long-shaped dataframe.
At this point you'll observe that "year" column has ugly entries like
"gdp2021". There are multiple ways you can fix this:
    
    - Don't use melt()! Use wide_to_long() instead, looking up how it works
    online: https://pandas.pydata.org/docs/user_guide/reshaping.html
    - Use map() or apply() to fix this by the application of function, maybe
    even a lambda function
    - Use df["x"].str to "vectorize" the column x in dataframe df. You can now
    apply any string function the way you normally would e.g. df["x"].str.upper()
    The method astype(int) can convert str to int
    
The choice of this is left to you. You can pick one at random by choosing
a random number from 1 to 3 at https://www.random.org
"""

"""
EXERCISE 2

Short: Do the same for the population data

Long: This does not require a longer explanation 
"""

"""
EXERCISE 3

Short: Merge the two data frames using the crosswalk provided in L09_data_crosswalk.csv

Long: It appears that the two dataset identify the state using different 
techniques. The population data uses the abbreviation of the state's name. The
GDP data uses a number to identify it - specifically it uses the FIPS
code: https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards

Create a dataframe that merges the gdp dataframe with the crosswalk using "state_id"
in the gdp dataframe and "FIPS" in the crosswalk dataframe. Then merge df with the 
population df using "Abbreviation" in df and "state" in the population dataframe.
"""

"""
EXERCISE 4

Short: Clean the data up, removing extraneous columns and reordering it so that
it goes: state, year, then the two economic indicators

Long: Use .drop to get rid of any columns you no longer want e.g. state_id. 
Reordering is done by passing through a list of column names arranged
in the desired order.
"""

"""
BONUS

- Find the GDP per capita. The gdp presented is in billions and the population 
is in millions

- Use the sort_values method to arrange it neatly, first by state and then by 
year
 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
"""