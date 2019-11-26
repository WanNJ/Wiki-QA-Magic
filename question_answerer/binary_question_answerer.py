import sys

sys.path.append("..")
import util_service


def get_answer(question, localized_statement):
    """
    gets answer to the binary question
    TODO: HOW?
    """

    # print(question)
    # print(util_service.get_dependency_parse(question))
    # print(localized_statement)
    # print(util_service.get_dependency_parse(localized_statement))

    # negation = 1 #either 1 or -1, flips sign if finds a "not" or "no" in question

    ner_only = util_service.get_ner(question)

    probably_the_subject = ner_only[0][0]

    subject_start_i = question.find(probably_the_subject)
    subject_end_i = subject_start_i + len(probably_the_subject)  # removes the first named entity
    q_no_sub = question[subject_end_i:len(question)]

    negatives = ["no", "not", "without"]

    if q_no_sub in localized_statement:
        for negative in negatives:
            if negative in localized_statement:
                return "No"
    return "Yes"
