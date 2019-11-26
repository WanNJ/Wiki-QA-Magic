import sys
sys.path.append("..")
import util_service


def localized_statement_pipeline(localized_statement):
    localized_dep_parse = util_service.get_dependency_parse(localized_statement)
    root_idx = localized_dep_parse.index("ROOT")
    ner_tokens = util_service.get_ner_per_token(localized_statement)

    return localized_dep_parse, root_idx, ner_tokens


def get_attitude_and_subj(question, localized_statement):
    a_doc, _ = util_service.get_dep_parse_tree(localized_statement)

    # Identify the subject of the localized statement
    subj_head = None
    for token in a_doc:
        if token.dep_ == 'nsubj':
            subj_head = token

    subj = subj_head
    # Use the noun chunk as the answer instead of a single word.
    if subj_head is not None:
        for chunk in a_doc.noun_chunks:
            if chunk.root.i == subj_head.i:
                subj = chunk.text
                break

    if "not" in question or "n't" in question or "no" in question:
        return False, subj
    else:
        return True, subj


def get_do_answer(question, localized_statement):
    attitude, subj = get_attitude_and_subj(question, localized_statement)

    if not subj:
        if attitude:
            return "Yes."
        else:
            return "No."

    if attitude:
        return "Yes, %s do." % subj
    else:
        return "No, %s don't." % subj


def get_does_answer(question, localized_statement):
    attitude, subj = get_attitude_and_subj(question, localized_statement)

    if not subj:
        if attitude:
            return "Yes."
        else:
            return "No."

    if attitude:
        return "Yes, %s does." % subj
    else:
        return "No, %s doesn't." % subj


def get_did_answer(question, localized_statement):
    attitude, subj = get_attitude_and_subj(question, localized_statement)

    if not subj:
        if attitude:
            return "Yes."
        else:
            return "No."

    if attitude:
        return "Yes, %s did." % subj
    else:
        return "No, %s didn't." % subj


def get_answer(question, localized_statement):
    """
    Get answers to the WH question
    """
    ans = None
    if question.split()[0].lower() == "do":
        ans = get_do_answer(question, localized_statement)

    elif question.split()[0].lower() == "does":
        ans = get_does_answer(question, localized_statement)

    elif question.split()[0].lower() == "did":
        ans = get_did_answer(question, localized_statement)

    return ans
