from typing import Final  # Used to define constants
import requests
import os

# Final[str] specifies that API_KEY is immutable after initialization, cant change going forward.
# API_KEY caps as constant.
API_KEY: Final[str] = "3d4824bd829bbb35795338fc0d689e76da3d1" 
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link} # payload: settings we use when we make a request, its dict type
    request = requests.get(BASE_URL, params=payload) # GET request, you will get the response in 'request'.
    # r = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(key, url)) # Can use this in url too instead of params
    data: dict = request.json()  # request.json() will convert response to json type
    # print(data)
    # {'url': {'status': 7, 'fullLink': 'https://leetcode.com/', 'shortLink': 'https://cutt.ly/TwBCeDrI'}}

    if url_data := data.get('url'):  # assignment expression operator (:=), also known as the "walrus operator"
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print("short link is : ", short_link)
        else:
            print('Error Status:', url_data['status'])

# data.get('url'): This is a dictionary method that attempts to retrieve the value associated with the key 'url'
# from the dictionary data. If the key exists, the method returns the corresponding value; otherwise, it returns None.
#
# url_data := data.get('url'): It allows you to assign a value to a variable as part of an expression. This can be
# particularly useful in situations where you want to both assign a value to a variable and use that value in a
# subsequent operation, all within a single line of code. Also when you want to check if the value exists or not


def main():
    input_link: str = input("Enter a link: \n")
    shorten_link(input_link)


if __name__ == '__main__':  # If this file is imported, this will not run
    main()

# When Python runs a script, it sets a special variable called "__name__" to "__main__" if the script is being executed
# directly. If the script is imported as a module into another script, the __name__ variable is set to
# the name of the module.

# Thus, when you see if __name__ == '__main__':, it means that the code inside this block will only execute if
# the script is being run directly, not if it's imported as a module.
