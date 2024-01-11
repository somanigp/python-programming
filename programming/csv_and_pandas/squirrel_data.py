import pandas as pd

data = pd.read_csv("squirrel_data.csv")
# to get how many squirrel are of each color
# print(data)

# count_of_gray = len(data[data["Primary Fur Color"] == "Gray"])  # df are kind of iterables, thus len gives total rows
# print(count_of_gray)

count_of_each_fur_color = data["Primary Fur Color"].value_counts()  # Return a Series containing counts of unique values
# print(type(count_of_each_fur_color))  # <class 'pandas.core.series.Series'>

dict_of_count = count_of_each_fur_color.to_dict()  # converting a series to dict
# print(dict_of_count)

# Only a certain type of data can be converted to df
dict_to_convert = {
    "fur color": [],
    "count": []
}
for key in dict_of_count:
    dict_to_convert["fur color"].append(key)  # dict_to_convert["fur color"] fetches the empty list and we can add to it
    dict_to_convert["count"].append(dict_of_count[key])

print(dict_to_convert)
data = pd.DataFrame(dict_to_convert)
print(data)
data.to_csv("./count_by_furs.csv")
