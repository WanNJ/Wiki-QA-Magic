import re

from . import question_type_identifier
from . import constants
from . import binary_question_answerer
from . import wh_question_answerer
from . import eo_question_answerer
from . import sentence_localizer

import sys

sys.path.append("..")
import util_service


def get_answers(wiki_text_block, questions):
    """
    returns the answers to questions based on the wiki text
    Contains only business logic, WHAT to do rather than HOW to do.
    Common helper functions to be accessed from util_service module.
        :param text: Wikipedia text
        :questions: list of questions
    """
    # Steps
    # 1 - coref resolution
    # 2 - find similar sentences for question, localization, 
    #     need to come up with the threshold if the answer is not present in the para
    # 3 - Find the question type

    #   1. YES NO {is the population of Pittsburg 10000}
    #   2. Either/or {eg - does he like x or y}
    #   3. Wh question - {When, Where, Why,}
    # 4 get answers based on the question type

    # Step 1
    # coref_text = util_service.get_coref(wiki_text_block)

    # Step 2
    # loop over questions 
    answers = []
    for question in questions:

        localized_statement = sentence_localizer.get_localized_statement(question, wiki_text_block).strip()
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

        if answer is None or answer == constants.UNABLE_TO_ANSWER:
            answers.append("I don't know the answer.")
        else:
            answers.append(answer + ".")
    return answers
