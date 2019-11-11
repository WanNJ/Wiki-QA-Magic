import sys
sys.path.append("..")
import util_service

import numpy as np
from question_generator.qg_helpers import preprocess
from question_generator.qg_helpers import postprocess
from question_generator.qg_helpers import sentence_simplifier
from question_generator.qg_helpers import sentence_filterer
from question_generator.qg_helpers import question_type_identifier
from question_generator.qg_helpers import qg_constants

# Question generators
from question_generator.qtype_handlers import howmany_generator
from question_generator.qtype_handlers import what_generator
from question_generator.qtype_handlers import when_generator
from question_generator.qtype_handlers import who_generator
from question_generator.qtype_handlers import is_generator
from question_generator.qtype_handlers import where_generator


def get_questions(wiki_text, no_of_questions):
    """
    generates the questions based on the wiki text.
    Contains only business logic, WHAT to do rather than HOW to do.
    Common helper functions to be accessed from util_service module.
        :param wiki_text: string of a wikipedia article
        :param no_of_questions: int for number of questions
    """
    question_list = []

    # Step 0 - remove unnecessary characters
    wiki_text = preprocess.clean_text(wiki_text)
   
    # Step 1. coref resolution
    wiki_text = util_service.get_coref(wiki_text)

    # Step 2. break compound sentences to simple sentences
    # TODO
    wiki_text_sent_list = sentence_simplifier.simplify(wiki_text)

    # Step 3. filter sentences based on length, TODO and other parameters  
    filtered_wiki_text_sent_list = sentence_filterer.filter(wiki_text_sent_list)

    # Step 4: possible question type identifier
    possible_qs_per_sent_list = question_type_identifier.get_possible_question_types(filtered_wiki_text_sent_list)
    # print(possible_qs_per_sent_list)

    # Step 5: call question generators based on the qs types
    for idx in range(len(filtered_wiki_text_sent_list)):
        possible_qs_types = possible_qs_per_sent_list[idx]
        sentence = filtered_wiki_text_sent_list[idx]

        questions_for_sentence = []
        for q_type in possible_qs_types:
            if q_type == qg_constants.IS_QUESTION:
                questions = is_generator.generate_question(sentence)
            elif q_type == qg_constants.WHAT_QUESTION:
                questions = what_generator.generate_question(sentence)
            elif q_type == qg_constants.WHEN_QUESTION:
                questions = when_generator.generate_question(sentence)
            elif q_type == qg_constants.HOWMANY_QUESTION:
                questions = howmany_generator.generate_question(sentence)
            elif q_type == qg_constants.WHERE_QUESTION:
                questions = where_generator.generate_question(sentence)
            questions_for_sentence += questions

        question_list += list(set(questions_for_sentence))

    # Step 5. get ranking from question evaluator for generated questions
    # TODO:

    # Step 6. return ranked questions based on the no of questions
    question_list = postprocess.get_questions_by_no(question_list, no_of_questions)

    return question_list

# if __name__ == "__main__":

#     #print(get_questions("This is an article about Evan Kaaret. He is 22, halfway to 23. This is to test if the program spacy will correctly found out that he refers to Evan.", 1))
#     print(get_questions("President Evan is the subject of this article. He is 22, halfway to 23. This is to test if the program spacy will correctly found out that he refers to Evan.", 4))
#     #print(get_questions("Who is that.", 1))

if __name__ == "__main__":
    with open('/Users/gauravshegokar/Documents/CMU/FALL_2019/NLP/project/Wiki-QA-Magic/data/Development_data/set1/a1.txt', 'r') as content_file:
        wiki_text = content_file.read()
    get_questions(wiki_text, 10)
