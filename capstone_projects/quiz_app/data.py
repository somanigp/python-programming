import requests
# NOTE:** If here it is not a function and just a plain file getting the response and storing the result in
# question_data variable, then also if we import the variable question_data in main.py, everything works.
# This file is fully executed.


def generation_question_data() -> list:  # Write way.
    """Returns a list of questions with answers"""
    params = {
        "amount": 10,
        "category": 14,
        "difficulty": "medium",
        "type": "boolean"
    }
    # https://opentdb.com/api.php?amount=20&category=14&difficulty=medium&type=boolean
    # Note: In above url medium and boolean are string values, but when passing as url, they can be passed as this.
    response = requests.get(url="https://opentdb.com/api.php", params=params)
    try:
        response.raise_for_status()
    except Exception as e:
        print(f"The error is {e}")
    else:
        data = response.json()["results"]
        return data
    return []
