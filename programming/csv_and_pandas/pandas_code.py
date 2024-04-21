import pandas as pd
# API reference is all the things you can do with the lib. https://pandas.pydata.org/docs/reference/index.html

data = pd.read_csv("weather_data.csv")
print(type(data))  # <class 'pandas.core.frame.DataFrame'>

# 2 primary data structure of pandas
# 1. Series: 1-dimensional; A single column
# 2. Dataframe: 2-dimensional; Every single sheet inside Excel file

print(type(data["temp"]))  # <class 'pandas.core.series.Series'>

# convert df to dict
data_dict = data.to_dict()
print(data_dict)

# convert series to list
data_list = data["temp"].to_list()
print(data_list)

avg_temp = sum(data_list)/len(data_list)
print(round(avg_temp, 2))  # up to decimal 2

# to calc avg of a series
print(data["temp"].mean())  # NOTE: col name is by default the first name of the data

# to get max value in the series
print(data["temp"].max())

# get data in col
# print(data["condition"])
print(data.condition)  # each of the col headings is converted to attributes

# Get data in a row - when you apply filters you get the row instead
print(data[data.day == "Monday"])  # give from data where data.day == "Monday"
print(data[data.temp == data.temp.max()])  # where data.temp is max

monday = data[data.day == "Monday"]  # monday is a row
print(monday.condition)  # operating on a row. can access attributes through this, as it's a df.

# print(monday.temp.to_list())  # list with only one int value
# print(type(monday.temp))  # <class 'pandas.core.series.Series'>
in_fahrenheit = (monday.temp[0] * (9/5)) + 32  # NOTE: through indexing in a series we can get the value.
print(in_fahrenheit)

# NOTE: df -> like dict: dict["col_name"][index] and series like list: list[index]

# Create a df from scratch
data_dict = {
    "students": ["Govind", "Anant", "Aman"],  # col_name as index and values as list.
    "scores": [100, 50, 0]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("./student_scores.csv")  # Create a csv file. Needs path as an input.

# age_no_na = titanic[titanic["Age"].notna()]
# The notna() conditional function returns a True for each row the values are not a Null value. As such, this can be combined with the selection brackets [] to filter the data table.
# adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
# In this case, a subset of both rows and columns is made in one go and just using selection brackets [] is not sufficient anymore. The loc/iloc operators are required in front of the selection brackets []. When using loc/iloc, the part before the comma is the rows you want, and the part after the comma is the columns you want to select. 

# I’m interested in rows 10 till 25 and columns 3 to 5.
# titanic.iloc[9:25, 2:5]
