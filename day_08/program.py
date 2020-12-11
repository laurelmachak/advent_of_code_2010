# {operation: 'jmp', arg: '-5', visted: False}
instructions = []


with open('data.txt', 'r') as f:
    for line in f:
        instr = {}
        line = line.strip().split(" ")
        instr['operation'] = line[0]
        instr['arg'] = line[1]
        instr['visited'] = False
        instructions.append(instr)


def acc(instr):
    number_str = instr['arg']
    sign = number_str[0]
    number = int(number_str[1:])
    val_change = 0

    if sign == '+':
        val_change += number
    else:
        val_change -= number
    
    return val_change

def jmp(instr, current_index):
    val_change = acc(instr)
    return current_index + val_change


# accumilator = 0
# current_index = 0
# visited_indexes = []


# while True:
#     instr = instructions[current_index]
#     if instr['visited']:
#         print('Already visited: ', instr)
#         print('accumilator: ', accumilator)
#         print("current_index: ", current_index)
#         break

#     elif instr['operation'] == 'acc':
#         accumilator += acc(instr)
#         current_index += 1
#         instr['visited'] = True

#     elif instr['operation'] == 'jmp':
#         instr['visited'] = True
#         current_index += acc(instr)

#     elif instr['operation'] == 'nop':
#         instr['visited'] = True
#         current_index += 1

#     visited_indexes.append(current_index)

#     if len(visited_indexes) == len(instructions):
#         print('***Made it all the way through!***')
#         print('accumilator: ', accumilator)



for i in range(len(instructions)):
    if instructions[i]['operation'] == 'jmp':
        instructions[i]['operation'] = 'nop'
    
    elif instructions[i]['operation'] == 'nop':
        instructions[i]['operation'] = 'jmp'

    accumilator = 0
    current_index = 0
    visited_indexes = []
    # print(i)


    while True:
        # print('current_index: ', current_index)
        try:
            instr = instructions[current_index]
        except:
            break

        if current_index in visited_indexes:
            # print('Already visited: ', instr)
            # print('accumilator: ', accumilator)
            # print("current_index: ", current_index)
            

            # print(visited_indexes)
            if instructions[i]['operation'] == 'jmp':
                instructions[i]['operation'] = 'nop'
    
            elif instructions[i]['operation'] == 'nop':
                instructions[i]['operation'] = 'jmp'

            break

        elif instr['operation'] == 'acc':
            visited_indexes.append(current_index)
            accumilator += acc(instr)
            current_index += 1
            instr['visited'] = True

        elif instr['operation'] == 'jmp':
            visited_indexes.append(current_index)
            instr['visited'] = True
            current_index += acc(instr)

        elif instr['operation'] == 'nop':
            visited_indexes.append(current_index)
            instr['visited'] = True
            current_index += 1

        # visited_indexes.append(current_index)

        if current_index == len(instructions):
            print(current_index)
            print('***Made it all the way through!***')
            print('accumilator: ', accumilator)
            print(current_index)
            break

    if current_index == len(instructions):

        break
    
    

# print(visited_indexes)


# for i in range(len(instructions)):
#     if instructions[i]['operation'] == 'acc':
        
#         accumilator += acc(instructions[i])
#         print(accumilator, acc(instructions[i]))


# # print(instructions)
# print(accumilator)