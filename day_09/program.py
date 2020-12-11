xmas = []

with open('data.txt', 'r') as f:
    for line in f:
        xmas.append(int(line.strip()))




def get_prev_chunk(current_index, chunk_size):
    return xmas[current_index-chunk_size:current_index]

def num_sum_in_prev_chunk(current_index, chunk_size):
    prev_chunk = get_prev_chunk(current_index, chunk_size)
    current_num = xmas[current_index]

    for i in range(len(prev_chunk)):
        diff = current_num - prev_chunk[i]
        if (diff != prev_chunk[i]) and (diff in prev_chunk):
            return True
    
    return False

def find_invalid_number():
    preamble_length = 25
    current_index = preamble_length

    for i in range(preamble_length, len(xmas)):
        if not num_sum_in_prev_chunk(i, preamble_length):
            return xmas[i]

def find_cont_range():
    invalid_number = find_invalid_number()
    
    for i in range(len(xmas)):
        sum = 0
        current_range = []
        for x in range(len(xmas)):
            offset_index = i+x
            sum += xmas[offset_index]
            current_range.append(xmas[offset_index])
            if sum > invalid_number:
                break
            if sum == invalid_number:
                return current_range


cont_range = find_cont_range()

print(min(cont_range) + max(cont_range))

# print(len(get_prev_chunk(current_index, preamble_length)))
# print(xmas[current_index])