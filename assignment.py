import json


def get_data(filename):
    with open(filename , "r") as f:
        data = json.load(f)

    # print(data)
    return data


data = get_data("data.json")

for user in data:
    print(user["rating"])
