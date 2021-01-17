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
        curr_questions = set()
        for line in group:
            curr_questions.update(set(line.strip()))
        unique_question_count += len(curr_questions)

    print(unique_question_count)
