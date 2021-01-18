with open("input_6.txt") as f:
    groups = []
    curr_group = []
    for line in f.readlines():
        if line == "\n":
            groups.append(curr_group)
            curr_group = []
        else:
            curr_group.append(line)

    unique_question_count = 0
    for group in groups:
        curr_questions = set(group[0].strip())
        for i in range(1, len(group)):
            line = group[i]
            curr_questions = curr_questions.intersection(set(line.strip()))
        unique_question_count += len(curr_questions)

    print(unique_question_count)
