import sys

with open("input_1.txt") as f:

    # Part 1:

    # nums = {int(string) for string in f.readlines()}
    # for num in nums:
    #     if 2020 - num in nums:
    #         print(num * (2020 - num))
    #         sys.exit()

    # Part 2:

    nums = [int(string) for string in f.readlines()]
    pair_sums = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            pair_sums[nums[i] + nums[j]] = (nums[i], nums[j])
    for num in nums:
        if (deficit := (2020 - num)) in pair_sums:
            print(num * pair_sums[deficit][0] * pair_sums[deficit][1])
            sys.exit()
