import sys
sys.path.append("..")
import util_service

def get_what_answer(question, localized_statement):
    pass

def get_when_answer(question, localized_statement):
    pass

def get_where_answer(question, localized_statement):
    """
    baseline where answer generator, needs to improved and tested across various test cases
    """
    # print(question)
    # print(localized_statement)
    localized_dep_parse = util_service.get_dependency_parse(localized_statement)
    # print(localized_dep_parse)
    root_idx = localized_dep_parse.index("ROOT")
    # print(util_service.get_ner(localized_statement))
    ner_tokens = util_service.get_ner_per_token(localized_statement)
    # print(ner_tokens)

    for x in ner_tokens[root_idx:]:
        if x[1] == "GPE":
            return x[0]
    return None

def get_who_answer(question, localized_statement):
    pass

def get_whom_answer(question, localized_statement):
    pass

def get_which_answer(question, localized_statement):
    pass

def get_whose_answer(question, localized_statement):
    pass

def get_why_answer(question, localized_statement):
    pass

def get_how_answer(question, localized_statement):
    pass



def get_answer(question, localized_statement):
    """
    gets answer to the WH question
    TODO: HOW?
    """
    if (question.split()[0].lower() == "where"):
        ans = get_where_answer(question, localized_statement)

    elif(question.split()[0].lower() == "what"):
        ans = get_who_answer(question, localized_statement)

    elif(question.split()[0].lower() == "when"):
        ans = get_when_answer(question, localized_statement)

    elif(question.split()[0].lower() == "who"):
        ans = get_who_answer(question, localized_statement)

    elif(question.split()[0].lower() == "whom"):
        ans = get_whom_answer(question, localized_statement)

    elif(question.split()[0].lower() == "which"):
        ans = get_which_answer(question, localized_statement)

    elif(question.split()[0].lower() == "whose"):
        ans = get_whose_answer(question, localized_statement)

    elif(question.split()[0].lower() == "why"):
        ans = get_why_answer(question, localized_statement)

    elif(question.split()[0].lower() == "how"):
        ans = get_how_answer(question, localized_statement)

    return ans