import bisect

"first 7 chars: F or B ---> reveal which row 0-127"
"last 3 chars: L or R ---> reveal which column 0-7"
"ID: (row * 8) + column"

seats = []

with open("data.txt", 'r') as f:
    for line in f:
        seats.append(line.strip())


def find_row(id):
    min = 0
    max = 127
    mid = (min + max)//2

    # F is lower B is upper half
    for char in id[0:7]:
        if char == 'F':
            max = mid
            mid = (min + max) // 2
        
        if char == 'B':
            min = mid + 1
            mid = (min + max) // 2
    
    return mid


def find_column(id):
    min = 0
    max = 7
    mid = (min + max) // 2

    # L is lower R is upper half
    for char in id[7:]:
        if char == "L":
            max = mid
            mid = (min + max) // 2

        if char == 'R':
            min = mid + 1
            mid = (min + max) // 2
    
    return mid


    

def find_seat_id(id):
    row = find_row(id)
    col = find_column(id)
    return (row * 8) + col


print(seats)

all_seat_ids = []

for seat in seats:
    bisect.insort(all_seat_ids, find_seat_id(seat))


for i in range(len(all_seat_ids)):
    current_id = all_seat_ids[i]
    next_id = all_seat_ids[i+1]
    if current_id + 1 != next_id:
        print(current_id, next_id)
        break
    


# print(all_seat_ids)

# highest_id = 0

# for seat in seats:
#     if find_seat_id(seat) > highest_id:
#         highest_id = find_seat_id(seat)

# print(highest_id)


