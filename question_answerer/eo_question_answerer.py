import sys

sys.path.append("..")
import util_service


def get_answer(question, localized_statement):
    """
    This is super bad. It finds the possible answers,
    (aka everything past the first named entity, then splits
    that for stuff before and after the or statements in the question),
    then looks for the statement that occurred first. I want to make it
    so it looks for similarity and not a perfect comparison of strings
    """
    ner_only = util_service.get_ner(question)

    probably_the_subject = ner_only[0][0]

    subject_start_i = question.find(probably_the_subject)
    subject_end_i = subject_start_i + len(probably_the_subject)  # removes the first named entity
    q_no_sub = question[subject_end_i:len(question)]
    ner_tokens_q_no_sub = util_service.get_ner_per_token(q_no_sub)

    # This gets the possible answers by finding the words right before "or"
    # Does this on the string without the named entity, ie:
    #   "Is Pittsburgh a city" --> "a city"
    possible_answers = []
    last_or_index = 0
    j = 0
    for i in range(len(ner_tokens_q_no_sub)):
        if ner_tokens_q_no_sub[i][0] == "or":
            last_or_index = i
            question_str = ""
            while j < i:
                question_str = question_str + ner_tokens_q_no_sub[j][0] + " "
                j += 1
            possible_answers.append(question_str)
            j = last_or_index

    # For the last answer after the last or
    j = last_or_index + 1
    question_str = ""
    while j < len(ner_tokens_q_no_sub):
        question_str = question_str + ner_tokens_q_no_sub[j][0] + " "
        j += 1
    question_str = question_str[0:len(question_str) - 2]  # gets rids of ?
    possible_answers.append(question_str)

    # idk calling .strip() on the list elements for possible_answers = possible_answers.strips()
    # didn't work
    new_pos_answers = []
    for answer in possible_answers:
        new_pos_answers.append(answer.strip())  # MAKE BETTER

    possible_ans_index = 0

    current_closest = len(localized_statement)
    for index, answer in enumerate(new_pos_answers):
        answer_index = localized_statement.find(answer)
        if answer_index < current_closest and answer_index > 0:
            current_closest = answer_index
            possible_ans_index = index

    # return probably_the_subject + " " + new_pos_answers[possible_ans_index]
    return new_pos_answers[possible_ans_index]
