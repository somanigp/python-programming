# https://pandas.pydata.org/docs/getting_started/index.html
# CSV - comma separated values (a way to represent tabular data). Each row is a single set of data,
# and it is separated by ','

# data = []
# with open("weather_hour_data.csv") as csv:
#     for i in csv.readlines():
#         data.append(i.strip())
#
# print(data)

import csv  # in-built library for csv.

# Using alias for pandas lib
import pandas as pd  # as it's not an in-built lib, we need to install this package.

with open("weather_data.csv") as data_file:  #
    temperatures = []  # can declare variables in if/while/with etc.
    data = csv.reader(data_file)  # read csv file and op the data
    print(data)  # <_csv.reader object at 0x00000273C38CD180>
    # _csv.reader object - can be looped through
    for row in data:  # data[1:] - is not valid as cant concat csv.reader objects
        # print(row)  # each row is stored as list obj like ['day', 'temp', 'condition'] and ['Monday', '12', 'Sunny']
        if row[1] == "temp":
            continue  # skip that iteration
        temperatures.append(int(row[1]))

    print(temperatures)

# 'pandas' lib makes it even easier to work with data in tabular or other forms.
# helps perform data analysis on tabular data.

# In pandas, a data table is called a DataFrame.

# Pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. Pandas support
# many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), each of them with
# the prefix read_*

csv_data = pd.read_csv("weather_data.csv")
# When displaying a DataFrame, the first and last 5 rows will be shown by default
# print(csv_data)
print(csv_data["temp"])  # column name x[col_name] to get hold of a series.
print(type(csv_data[["day", "temp"]]))  # Single col (single string as col name is passed) - series. when list is passed
# meaning multiple columns - return data type is dataFrame

# Each column in a DataFrame is a Series. As a single column is selected, the returned object is a pandas Series.
# 'dtype': column data types
# integers (int64), floats (float64) and strings (object)

print(csv_data.shape)  # DataFrame.shape is an attribute (func needs '()').
# containing the number of rows and columns: (nrows, ncolumns).

print(csv_data["temp"].shape)  # shape of that 1 selected col. Thus col size is 1

print(csv_data[csv_data["temp"] > 13])  # here it returns the whole table with this filter
# filters, series or dataframe will be returned according to this
