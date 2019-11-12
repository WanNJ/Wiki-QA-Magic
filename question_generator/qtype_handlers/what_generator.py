import sys
sys.path.append("../..")
import util_service

from question_generator.qtype_handlers.get_is_are_was_were_loc import which_acomp

def generate_question(sentence):

    # "is", "as a", "FAC", 
    # NEEDS "was", "were", "are"

    ner_tokens_sentence = util_service.get_ner_per_token(sentence)
    ner_only = util_service.get_ner(sentence)

    if len(ner_only) == 0:
        return []

    # Finds where the is word is, then is just going to append everything after it 
    # into a question
    is_are_index = -1
    # flag is a string (one of "Is ", "Are ", "Was ", or "Were ")
    # is_are_index is where this string occurs in the tokens

    flag, is_are_index = which_acomp(ner_tokens_sentence)
    if flag == "":
        return []
    new_question = "What " + flag + "the " + ner_only[0][0] + "?"

    # q_dep_parse = util_service.get_dependency_parse(sentence)
    # print(q_dep_parse)
    # print(ner_tokens_sentence)

    return_list = [] # Is the return supposed to be a list? I guess multiple possible questions
    return_list.append(new_question)
    return return_list

# a = generate_question("The Old Kingdom is most commonly regarded as the period from the Third Dynasty through to the Sixth Dynasty 2686–2181 BC")
# # This was to see the dep parse of is, are, was, were
# b = generate_question("Chips are tasty. Food is good. Blocks and cheese are food. I was in America. They were outside.")
