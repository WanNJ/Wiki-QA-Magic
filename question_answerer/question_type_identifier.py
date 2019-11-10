import sys
sys.path.append("..")
import util_service
from . import constants


def is_wh_question(question, dependency_parse):
    """
    Baseline wh question identifer.
    TODO: Need to work with dependency parse information to be more confidant.
    Completed just for the sake of the pipeline building.

    Inputs:
        question: string, the question, ie "Where is Pittsburgh located?"
        dependency_parse: 
    """
    wh_questions = ["what", "when", "where", "who", "whom", "which", "whose", "why", "how"]

    if question.split()[0].lower() in wh_questions:
        return True
    return False


def is_either_or_question(question, dependency_parse):
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

    if (question_list[0].lower() in eo_indicator_start
        and "or" in question_list):
        return True
    return False


def is_binary_question(question, dependency_parse):
    """
    

    Example binary question: Is Evan 1?

    Inputs: question: list of strings: each element of the list is a string, the last
                    element may also have a question mark. 
                    Ex: ['Where', 'is', 'Pittsburgh', 'located?']
        dependency_parse: list of the parse for the question
                    Ex: ['advmod', 'auxpass', 'nsubjpass', 'ROOT', 'punct']
    """

    binary_indicators = ["are", "is"] #are they 2. Is he 2
    # print("binary", question)
    if question.split()[0].lower() in binary_indicators:
        return True

    return False


def get_question_type(question):
    dependency_parse = util_service.get_dependency_parse(question)
    wh_question = is_wh_question(question, dependency_parse)
    either_or_question = is_either_or_question(question, dependency_parse)
    binary_question = is_binary_question(question, dependency_parse)

    if wh_question:
        return constants.WH_QUESTION
    if either_or_question:
        return constants.EITHER_OR_QUESTION
    if binary_question:
        return constants.BINARY_QUESTION
    return None
