import json

# opening json file
S = open('sample_data.json', 'r')

# return the json object as a dic
data = json.load(S)

# iterating through the json list
data_list = []
for i in data['parametersList']:
    my_dict = {
        "parameterName": i['parameterName'],
        "min": i['min'],
        "max": i['max'],
        "avg": i['avg']

    }

    data_list.append(my_dict)
my_list = json.dumps(data_list)

# dumps helps to convert it into json format, and it will return the string
print(my_list)

with open("input.json", 'w') as file1:
    file1.write(my_list)
print(data_list)

# closing file
S.close()
