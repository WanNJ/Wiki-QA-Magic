import sys
sys.path.append("..")
import util_service
from . import constants


def is_wh_question(question, dependency_parse):
    """
    Baseline wh question identifer.
    TODO: Need to work with dependency parse information to be more confidant.
    Completed just for the sake of the pipeline building.
    """
    wh_questions = ["what", "when", "where", "who", "whom", "which", "whose", "why", "how"]

    if question.split()[0].lower() in wh_questions:
        return True
    return False


def is_either_or_question(question, dependency_parse):
    """
    returns False as of now.
    TODO: Need to work with dependency parse information.
    Completed just for the sake of the pipeline building.
    """
    return False


def is_binary_question(question, dependency_parse):
    """
    returns False as of now.
    TODO: Need to work with dependency parse information.
    Completed just for the sake of the pipeline building.
    """
    return False


def get_question_type(question):
    dependency_parse = util_service.get_dependency_parse(question)
    wh_question = is_wh_question(question, dependency_parse)
    either_or_question = is_either_or_question(question, dependency_parse)
    is_binary_question = is_wh_question(question, dependency_parse)

    if wh_question:
        return constants.WH_QUESTION
    if either_or_question:
        return constants.EITHER_OR_QUESTION
    if is_binary_question:
        return constants.BINARY_QUESTION
    return None
