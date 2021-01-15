with open("input_5.txt") as f:
    # max_seat_id = 0
    # for seat_code in f.readlines():
    #     row = int(seat_code[:7].replace("F", "0").replace("B", "1"), 2)
    #     column = int(seat_code[7:].replace("R", "1").replace("L", "0"), 2)
    #     curr_seat_id = row * 8 + column
    #     max_seat_id = max(max_seat_id, curr_seat_id)

    # print(max_seat_id)
    all_ids = set(range(1024))
    current_ids = set()
    for seat_code in f.readlines():
        row = int(seat_code[:7].replace("F", "0").replace("B", "1"), 2)
        column = int(seat_code[7:].replace("R", "1").replace("L", "0"), 2)
        curr_seat_id = row * 8 + column
        current_ids.add(curr_seat_id)

    print(all_ids.difference(current_ids))
