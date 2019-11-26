import re

from . import question_type_identifier
from . import constants
from . import binary_question_answerer
from . import wh_question_answerer
from . import eo_question_answerer
from . import sentence_localizer
from . import do_question_answerer

import sys

sys.path.append("..")
import util_service


def get_answers(wiki_text_block, questions):
    """
    returns the answers to questions based on the wiki text
    Contains only business logic, WHAT to do rather than HOW to do.
    Common helper functions to be accessed from util_service module.
        :param wiki_text_block: Wikipedia text
        :questions: list of questions
    """
    # Steps
    # 1 - coref resolution
    # 2 - find similar sentences for question, localization, 
    #     need to come up with the threshold if the answer is not present in the para
    # 3 - Find the question type

    #   1. YES NO {is the population of Pittsburgh 10000}
    #   2. Either/or {eg - does he like x or y}
    #   3. Wh question - {When, Where, Why,}
    # 4 get answers based on the question type

    # Step 1
    clean_text = util_service.remove_title(wiki_text_block)
    coref_text = util_service.get_coref(clean_text)

    # Step 2
    # loop over questions 
    answers = []
    for question in questions:

        localized_statement = sentence_localizer.get_localized_statement(question, coref_text).strip()
        localized_statement = re.sub('\s+', ' ', localized_statement).strip()

        # Step 3: identify question type
        question_type = question_type_identifier.get_question_type(question)

        answer = None

        if question_type is None:
            answer = constants.UNABLE_TO_ANSWER

        # Step 4: Generate answers based on the question type
        if question_type == constants.BINARY_QUESTION:
            answer = binary_question_answerer.get_answer(question, localized_statement)
        elif question_type == constants.WH_QUESTION:
            answer = wh_question_answerer.get_answer(question, localized_statement)
        elif question_type == constants.EITHER_OR_QUESTION:
            answer = eo_question_answerer.get_answer(question, localized_statement)
        elif question_type == constants.DO_QUESTION:
            answer = do_question_answerer.get_answer(question, localized_statement)

        try:
            if answer:
                # Replace " to empty
                answer = str.replace(answer, '\"', '')
        except:
            pass

        if answer is None or answer == constants.UNABLE_TO_ANSWER:
            if localized_statement:
                # Return the entire localized statement(if exists) directly if unable to identify the question type
                answers.append(localized_statement)
            else:
                # If no statement can even be identified, return "I don't know the answer."
                answers.append("I don't know the answer.")
        else:
            # Make sure the answer ends in a period
            if not answer.endswith('.'):
                answer = answer + '.'
            answers.append(answer)

    return answers
