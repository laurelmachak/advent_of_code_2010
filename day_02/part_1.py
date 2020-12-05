test_data = "1-3 a: abcde,1-3 b: cdefg,2-9 c: ccccccccc"

#convert to a list:
string_list = test_data.split(',')
print(string_list)
# ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

def create_data_dict(data_string):
    # first seperate each comma seperated item to individual list item
    to_list = data_string.split(',')



passwords = []

with open('passwords.txt', 'r') as f:
    for line in f:
        item_dict = {}
        
        stripped_line = line.strip()
        end_min_index = stripped_line.index('-')
        end_max_index = stripped_line.index(' ')
        end_letter_index = stripped_line.index(':')

        item_dict['min'] = int(stripped_line[0:end_min_index])
        item_dict['max'] = int(stripped_line[end_min_index+1:end_max_index])
        item_dict['letter'] = (stripped_line[end_max_index+1:end_letter_index])
        item_dict['password'] = (stripped_line[end_letter_index+2:])
        # print(stripped_line[0:end_min_index])

        passwords.append(item_dict)


valid_passwords_part_1 = 0
valid = 0
for item in passwords:
    count = 0
    if item['password'][item['min']-1] == item['letter']:


        count += 1
    
    if item['password'][item['max']-1] == item['letter']:
        count += 1

    if count == 1:
        valid += 1
    




    count = item['password'].count(item['letter'])
    if (count>= item['min']) & (count<= item['max']):
        valid_passwords_part_1 +=1



# print(passwords)
print("shalom"[0:1])
print(passwords)
print(valid_passwords_part_1)

print(valid)
# print(len(passwords))