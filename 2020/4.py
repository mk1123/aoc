import re

with open("input_4.txt") as f:

    # part 1:

    passports = []
    curr_passport_lines = []
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    for line in f.readlines():
        if line == "\n":
            passports.append(curr_passport_lines)
            curr_passport_lines = []
        else:
            curr_passport_lines.append(line)
    all_passport_fields = []
    for passport in passports:
        categories = {}
        for line in passport:
            fields = line.split()
            for field in fields:
                colon_loc = field.index(":")
                categories[field[:colon_loc]] = field[colon_loc + 1 :]
        all_passport_fields.append(categories)
    count = 0
    for passport in all_passport_fields:
        valid = True
        if not required_fields.issubset(passport.keys()):
            continue
        for field, val in passport.items():
            if field == "byr":
                if not (len(val) == 4 and (1920 <= int(val) <= 2002)):
                    valid = False
                    break
            elif field == "iyr":
                if not (len(val) == 4 and (2010 <= int(val) <= 2020)):
                    valid = False
                    break
            elif field == "eyr":
                if not (len(val) == 4 and (2020 <= int(val) <= 2030)):
                    valid = False
                    break
            elif field == "hgt":
                last_two = val[-2:]
                if last_two == "cm":
                    if not (150 <= int(val[:-2]) <= 193):
                        valid = False
                        break
                elif last_two == "in":
                    if not (59 <= int(val[:-2]) <= 76):
                        valid = False
                        break
                else:
                    valid = False
                    break
            elif field == "hcl":
                if not re.compile(r"#[a-f0-9]+").search(val):
                    valid = False
                    break
            elif field == "ecl":
                if val not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                    valid = False
                    break
            elif field == "pid":
                if len(val) == 9:
                    try:
                        int(val)
                    except:
                        valid = False
                        break
                else:
                    valid = False
                    break
        if valid:
            count += 1
    print(count)
