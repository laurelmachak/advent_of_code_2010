data = []

with open('data.txt', 'r') as f:
    item = {}
    for line in f:
        
        if len(line) > 1:
            #not a blank line break
            line = line.strip()
            for entry in line.split(" "):
                key_val = entry.split(":")
                item[key_val[0]] = key_val[1]
        else:
            data.append(item)
            item = {}
    data.append(item)


has_requirements = []

def check_req_fields():
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    valid = 0
    invalid = 0
    for passport in data:
        count = 0
        for field in required_fields:
            
            if field in passport:
                count += 1
        if count == 7:
            valid += 1
            has_requirements.append(passport)
        else:
            invalid += 1
    
    return valid

def data_validation():
    valid = 0
    allowed_hcl_chars = "abcdef0123456789"
    allowed_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for passport in has_requirements:
        count = 0
        if (1920 <= int(passport["byr"]) <= 2002):
            count += 1

        if (2010 <= int(passport["iyr"]) <= 2020):
            count += 1

        if (2020 <= int(passport["eyr"]) <= 2030):
            count += 1

        if passport['hgt'][-2:] == "in":
            if (59 <= (int(passport['hgt'][0:-2])) <= 76):
                count += 1

        if passport['hgt'][-2:] == "cm":
            if (150 <= (int(passport['hgt'][0:-2])) <= 193):
                count += 1

        if (len(passport['hcl']) == 7) and (passport['hcl'][0] == '#'):
            if all(char in allowed_hcl_chars for char in passport['hcl'][1:]):
                count += 1

        if passport['ecl'] in allowed_ecl:
            count += 1

        if passport['pid'].isnumeric() and (len(passport['pid']) == 9):
            count += 1

        
        if count == 7:
            valid += 1

    return valid


# print(data)
print(check_req_fields())
print(len(has_requirements))
print(len("2222222"))

print(data_validation())