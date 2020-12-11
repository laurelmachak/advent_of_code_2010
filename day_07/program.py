# [some color] bags contain [amt] [some color] bag(s), [amt] [some color] bag(s)...
# [some color] bags contain no other bags


bag_rules = {}
test_split = []

def get_outer_color(line):
    end_color_string = line.index(' bags')
    return line[0:end_color_string]

def find_space_index(line, space_num):
    count = 0
    for i in range(len(line)):
        char = line[i]
        if char == " ":
            count += 1
            if count == space_num:
                return i



with open('data.txt', 'r') as f:
    for line in f:
        outer_color = get_outer_color(line)
        bag_rules[outer_color] = {}
        
        begin_contents_index = find_space_index(line, 4) + 1
        if line[begin_contents_index].isdigit():
            #contains bags, so split and get info
            contents = line[begin_contents_index:].strip().split(',')
            for rule in contents:
                rule = rule.strip()
                first_space = find_space_index(rule, 1)
                third_space = find_space_index(rule, 3)

                amt = rule[:first_space]
                color = rule[first_space + 1:third_space]
                bag_rules[outer_color][color] = amt


def find_direct_colors():
    direct_colors = []
    for key in bag_rules:
        if 'shiny gold' in bag_rules[key]:
            direct_colors.append(key)
            # print(key, bag_rules[key])

    print(direct_colors)
    return direct_colors

def find_sub_colors(color):
    count = 0
    sub_colors = []

    for key in bag_rules:
        if color in bag_rules[key]:
            if key not in sub_colors:
                sub_colors.append(key)
                count += 1
    print(sub_colors)
    return count

def indirect_colors(dir_colors):
    ind_colors = []
    for key in bag_rules:
        count = 0
        for color in dir_colors:
            if color in bag_rules[key]:
                count +=1
        if count >= 1:
            # print(count)
            ind_colors.append(key)
    
    return ind_colors


valid_bags = {}

def move_used_rules(items):
    for item in items:
        valid_bags[item] = bag_rules.pop(item) 




# direct_colors = find_direct_colors()

# print(len(bag_rules))
# move_used_rules(direct_colors)
# print(len(bag_rules))


# ind_colors = indirect_colors(direct_colors)
# print(ind_colors)
# move_used_rules(ind_colors)

# ind_colors_2 = indirect_colors(ind_colors)
# print(ind_colors_2)
# move_used_rules(ind_colors)


color_set = find_direct_colors()
move_used_rules(color_set)

while True:
    color_set = indirect_colors(color_set)
    move_used_rules(color_set)
    if len(color_set) == 0:
        break


print(len(valid_bags))
print('shiny gold' in valid_bags)


# final_count = len(direct_colors)

# for color in direct_colors:
#     final_count += find_sub_colors(color)

# print(final_count)

# print(direct_colors)
# print(len(direct_colors))
# print(len(bag_rules))




# print(test_split)
# 'shalom'.split(',')