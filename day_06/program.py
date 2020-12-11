
answers = []

with open('data.txt', 'r') as f:
    group = []

    for line in f:

        if len(line) > 1:
            #not a blank line
            group.append(line.strip())
        else:
            answers.append(group)
            group = []

    answers.append(group)



def group_yes_count(grp):
    # count = 0
    unique_letters = ""

    for string in grp:
        for char in string:
            if char not in unique_letters:
                unique_letters += char

    return len(unique_letters)

# print(answers)

def count_char_in_grp(grp, char):
    # in_all_items = True
    count = 0
    for item in grp:
        if char in item:
            count += 1

    return count


def chars_in_all_items(grp):
    letters = grp[0]
    total = 0
    for letter in letters:
        if count_char_in_grp(grp, letter) == len(grp):
            total += 1

    return total



# count = 0

# for grp in answers:
#     count += group_yes_count(grp)

count = 0

for grp in answers:
    count += chars_in_all_items(grp)

print(count)
    