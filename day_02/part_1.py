test_data = "1-3 a: abcde,1-3 b: cdefg,2-9 c: ccccccccc"

#convert to a list:
string_list = test_data.split(',')
print(string_list)
# ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

def create_data_dict(data_string):
    # first seperate each comma seperated item to individual list item
    to_list = data_string.split(',')
    