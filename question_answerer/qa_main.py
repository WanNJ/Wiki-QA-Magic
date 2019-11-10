from . import question_type_identifier
from . import constants
from . import binary_question_answerer
from . import wh_question_answerer
from . import eo_question_answerer
from . import sentence_localizer

import sys
sys.path.append("..")
import util_service

def get_answer(wiki_text_block, question):
    """
    returns the answer to question based on the wiki text
    Contains only business logic, WHAT to do rather than HOW to do.
    Common helper functions to be accessed from util_service module.
        :param text: Wikipedia text
    """
    # Steps
    # 1 - coref resolution
    # 2 - find similar sentences for question, localization, 
    #     need to come up with the threshold if the answer is not present in the para
    # 3 - Find the question type
        # 1. YES NO {is the population of Pittsburg 10000}
        # 2. Either/or {eg - does he like x or y}
        # 3. Wh question - {When, Where, Why,}
    # 4 get answers based on the question type 

    # print("Question: ", question)
    # Step 1
    coref_text = util_service.get_coref(wiki_text_block)

    # print("COREF: ", coref_text)

    # Step 2
    localized_statement = sentence_localizer.get_localized_statement(question, coref_text)
    # print("Localized_statement: ", localized_statement)

    # Step 3: identify question type
    question_type = question_type_identifier.get_question_type(question)
    # print("Question Type: ", question_type)
    if question_type == None:
        return constants.UNABLE_TO_ANSWER
    
    # Step 4: Generate answers based on the question type
    if question_type == constants.BINARY_QUESTION:
        answer = binary_question_answerer.get_answer(question, localized_statement)
    elif question_type == constants.WH_QUESTION:
        answer = wh_question_answerer.get_answer(question, localized_statement)
    elif question_type == constants.EITHER_OR_QUESTION:
        answer = eo_question_answerer.get_answer(question, localized_statement)

    return answer

