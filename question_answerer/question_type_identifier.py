import sys
sys.path.append("..")
from . import constants


def is_wh_question(question):
    """
    Baseline wh question identifier.
    TODO: Need to work with dependency parse information to be more confidant.
    Completed just for the sake of the pipeline building.

    Inputs:
        question: string, the question, ie "Where is Pittsburgh located?"
    """
    wh_questions = ["what", "when", "where", "who", "whom", "which", "whose", "why", "how"]

    if question.split()[0].lower() in wh_questions:
        return True
    return False


def is_either_or_question(question):
    """

    

    Example either or question: "Is Evan a banana or apple?"

    Inputs: question: list of strings: each element of the list is a string, the last
                        element may also have a question mark. 
                        Ex: ['Where', 'is', 'Pittsburgh', 'located?']
            dependency_parse: list of the parse for the question
                        Ex: ['advmod', 'auxpass', 'nsubjpass', 'ROOT', 'punct']
    """
    eo_indicator_start = ["are", "is"] # is pittsburgh blue or green. <-- starts with is, same as binary

    question_list = question.split()

    if question_list[0].lower() in eo_indicator_start and "or" in question_list:
        return True

    return False


def is_binary_question(question):
    """
    Example binary question: Is Evan 1?

    Inputs: question: list of strings: each element of the list is a string, the last
                    element may also have a question mark. 
                    Ex: ['Where', 'is', 'Pittsburgh', 'located?']
        dependency_parse: list of the parse for the question
                    Ex: ['advmod', 'auxpass', 'nsubjpass', 'ROOT', 'punct']
    """
    binary_indicators = ["are", "is", "were", "was", "am"]
    if question.split()[0].lower() in binary_indicators:
        return True

    return False


def is_do_question(question):
    do_indicators = ["do", "does", "did"]
    if question.split()[0].lower() in do_indicators:
        return True

    return False


def get_question_type(question):
    wh_question = is_wh_question(question)
    either_or_question = is_either_or_question(question)
    binary_question = is_binary_question(question)
    do_question = is_do_question(question)

    if wh_question:
        return constants.WH_QUESTION
    if either_or_question:
        return constants.EITHER_OR_QUESTION
    if binary_question:
        return constants.BINARY_QUESTION
    if do_question:
        return constants.DO_QUESTION
    return None
