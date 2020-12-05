tree_map = []

with open('map.txt', 'r') as f:
    for line in f:
        tree_map.append(list(line.strip()))
        # tree_map.append([line.strip()])



# empty = 0
# trees = 0

# for i in range(1, len(tree_map)):
#     index = (i*3) % len(tree_map[i])
#     if tree_map[i][index] == '#':
#         trees += 1
#     else:
#         empty += 1

# print('trees: ', trees)
# print('empty: ', empty)


def check_slope(r, d):
    start_index = 1
    trees = 0
    empty = 0
    for i in range(d, len(tree_map), d):
        index = (start_index * r) % len(tree_map[i])
        if tree_map[i][index] == '#':
            trees += 1
        else:
            empty += 1

        start_index += 1
    print('trees: ', trees)
    print('empty: ', empty)
    
    # return(trees, empty)
    return trees


print(tree_map)


a = check_slope(1, 1)
b = check_slope(3, 1)
c = check_slope(5, 1)
d = check_slope(7, 1)
e = check_slope(1, 2)

print(a*b*c*d*e)




