adapters = []

with open('test_data.txt', 'r') as f:
    for line in f:
        adapters.append(int(line.strip()))


adapters.sort()

#start at 0
#add 3 to the last one

# print(len(adapters)/4)
diffs = []

for i in range(len(adapters) - 1):
    diffs.append(adapters[i+1] - adapters[i])

print(adapters)
print(diffs)


# one_jolt_diffs = 1 # because first diff is 0 outlet +1
# three_jolt_diffs = 1 # because last diff is highest val +3


# for i in range(len(adapters) - 1):
#     if adapters[i+1] - adapters[i] == 1:
#         one_jolt_diffs += 1
    
#     elif adapters[i+1] - adapters[i] == 3:
#         three_jolt_diffs += 1


# print(adapters)
# print(len(adapters))
# print(72+37)
# print(one_jolt_diffs)
# print(three_jolt_diffs)
# print(one_jolt_diffs * three_jolt_diffs)