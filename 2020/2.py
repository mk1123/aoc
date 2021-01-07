with open("input_2.txt") as f:

    # part 1:

    # count = 0

    # for line in f.readlines():
    #     dash_loc = line.index("-")
    #     low = int(line[:dash_loc])
    #     space_loc = line.index(" ")
    #     high = int(line[dash_loc + 1 : space_loc])
    #     repeat_char = line[space_loc + 1]
    #     string = line[space_loc + 4 :]
    #     if low <= string.count(repeat_char) <= high:
    #         count += 1

    # print(count)

    # part 2:

    count = 0

    for line in f.readlines():
        dash_loc = line.index("-")
        first = int(line[:dash_loc])
        space_loc = line.index(" ")
        second = int(line[dash_loc + 1 : space_loc])
        char = line[space_loc + 1]
        string = line[space_loc + 4 :]
        if (string[first - 1] == char) ^ (string[second - 1] == char):
            count += 1

    print(count)

