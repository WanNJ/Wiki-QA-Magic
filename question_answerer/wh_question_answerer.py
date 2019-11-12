import sys


sys.path.append("..")
import util_service


def localized_statement_pipeline(localized_statement):
    localized_dep_parse = util_service.get_dependency_parse(localized_statement)
    root_idx = localized_dep_parse.index("ROOT")
    ner_tokens = util_service.get_ner_per_token(localized_statement)

    return localized_dep_parse, root_idx, ner_tokens


def get_what_answer(question, localized_statement):
    """
    Currently, the answerer use the part before ROOT of the localized statement as the answer to the question.
    TODO: Further improvement needs to be made.
    TODO: Wrong localized statement for question "What is pittsburgh?".
    :param question:
    :param localized_statement:
    :return:
    """
    answer = None
    a_doc, _ = util_service.get_dep_parse_tree(localized_statement)

    # Identify the subject of the localized statement
    a_subj_head = None
    for token in a_doc:
        if token.dep_ == 'nsubj':
            a_subj_head = token

    # Use the noun chunk as the answer instead of a single word.
    # if a_subj_head is not None:
    #     for chunk in a_doc.noun_chunks:
    #         if chunk.root.i == a_subj_head.i:
    #             answer = chunk.text
    #             break

    localized_dep_parse, root_idx, _ = localized_statement_pipeline(localized_statement)

    if a_subj_head.i < root_idx:
        answer = ' '.join(localized_statement.split(' ')[:root_idx])

    return answer


def get_when_answer(question, localized_statement):
    localized_dep_parse, root_idx, ner_tokens = localized_statement_pipeline(localized_statement)

    for x in ner_tokens[root_idx:]:
        if x[1] == "DATE":
            return x[0]

    return None



def get_where_answer(question, localized_statement):
    """
    baseline where answer generator, needs to improved and tested across various test cases
    """

    localized_dep_parse, root_idx, ner_tokens = localized_statement_pipeline(localized_statement)


    for x in ner_tokens[root_idx:]:
        if x[1] == "GPE":
            return x[0]


    return None


def get_who_answer(question, localized_statement):
    """
    baseline who answer generator, needs to improved and tested across various test cases
    """
    localized_dep_parse, root_idx, ner_tokens = localized_statement_pipeline(localized_statement)
    a_doc, _ = util_service.get_dep_parse_tree(localized_statement)

    for i, x in enumerate(ner_tokens):
        if x[1] == "PERSON" or x[1] == 'ORG':
            for chunk in a_doc.noun_chunks:
                if x[0] in chunk.text:
                    return chunk.text

    return None


def get_whom_answer(question, localized_statement):
    """
    Same logic as who question.
    TODO: Refine the implementation.
    :param question:
    :param localized_statement:
    :return:
    """
    return get_who_answer(question, localized_statement)


def get_whose_answer(question, localized_statement):
    """
    Same logic as who question.
    TODO: Refine the implementation.
    :param question:
    :param localized_statement:
    :return:
    """
    return get_who_answer(question, localized_statement)


def get_which_answer(question, localized_statement):
    """
    Same logic as what question.
    TODO: Refine the implementation.
    :param question:
    :param localized_statement:
    :return:
    """
    return get_what_answer(question, localized_statement)


def get_why_answer(question, localized_statement):
    """
    Just use the localized statement to provide useful information.
    TODO: Is there any better solutions?
    :param question:
    :param localized_statement:
    :return:
    """
    return localized_statement


def get_how_answer(question, localized_statement):
    """
    Just use the localized statement to provide useful information.
    TODO: Is there any better solutions?
    :param question:
    :param localized_statement:
    :return:
    """
    return localized_statement



def get_answer(question, localized_statement):
    """
    Get answers to the WH question
    """
    ans = None
    if question.split()[0].lower() == "where":
        ans = get_where_answer(question, localized_statement)

    elif question.split()[0].lower() == "what":
        ans = get_what_answer(question, localized_statement)

    elif question.split()[0].lower() == "when":
        ans = get_when_answer(question, localized_statement)

    elif question.split()[0].lower() == "who":
        ans = get_who_answer(question, localized_statement)

    elif question.split()[0].lower() == "whom":
        ans = get_whom_answer(question, localized_statement)

    elif question.split()[0].lower() == "which":
        ans = get_which_answer(question, localized_statement)

    elif question.split()[0].lower() == "whose":
        ans = get_whose_answer(question, localized_statement)

    elif question.split()[0].lower() == "why":
        ans = get_why_answer(question, localized_statement)

    elif question.split()[0].lower() == "how":
        ans = get_how_answer(question, localized_statement)

    return ans

