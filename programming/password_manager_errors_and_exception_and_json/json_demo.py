# JSON : JavaScriptObjectNotation
# https://docs.python.org/3/library/json.html
import json
# write - json.dump()
# read - json.load()
# update - json.update()

data = {"api1": {
    "version": 0,
    "date": "today"
}}
new_data = {"api2": {
    "version": 1,
    "date": "tmmr"
}}

try:
    # To Update:
    # Step 1: Load and Update the data
    with open("demo.json", mode="r") as data_file:
        # syntax - json.load(file: json)
        json_data = json.load(data_file)
        print(json_data)
        print(type(json_data))
        json_data.update(new_data)  # Updating the variable 'json_data'. No changes to the File
        print(json_data)
    # Step 2: Write Updated data to the file
    with open("demo.json", mode="w") as data_file:
        json.dump(json_data, data_file, indent=4)
except FileNotFoundError:
    with open("demo.json", mode="w") as data_file:
        # json.dump(data_object: dict,file: json, ..)
        json.dump(data, data_file, indent=4)  # indent - to make it readable
    print("file created")


# File "C:\Users\soman\AppData\Local\Programs\Python\Python312\Lib\json\decoder.py", line 355, in raw_decode
#     raise JSONDecodeError("Expecting value", s, err.value) from None
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

# ** Here it will be
# except json.decoder.JSONDecodeError: **NOTE**
