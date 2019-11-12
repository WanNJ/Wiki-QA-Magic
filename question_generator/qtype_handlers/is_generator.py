import sys
sys.path.append("../..")
import util_service

from get_is_are_was_were_loc import which_acomp

def generate_question(sentence):
    """
    Takes in a string sentence and generates a "Is" question.
    Puts "Is the " + named entity + rest_of_sentence + "?"
    """

    ner_tokens_sentence = util_service.get_ner_per_token(sentence)
    ner_only = util_service.get_ner(sentence)

    # Right now instead of this block it just adds "the " in the question later
    # This block would add "the " to the named entity if "the" is 
    # in the sentence right before where the named entity is
    # ner_start = ner_only[0][1]
    # list_of_the = ["The", "the"]
    # # sentence[ner_start - 4:ner_start] looks for "the"
    # if sentence[ner_start - 4 : ner_start-1] in list_of_the:
    #     ner_only[0][0] = "the " + ner_only[0][0]
        

    # print(ner_only)
    # print(ner_tokens_sentence)

    # No questions to be made without any named entities
    if len(ner_only) == 0:
        return []

    # Finds where the is word is, then is just going to append everything after it 
    # into a question
    is_are_index = -1
    # flag is a string (one of "Is ", "Are ", "Was ", or "Were ")
    # is_are_index is where this string occurs in the tokens
    flag, is_are_index = which_acomp(ner_tokens_sentence)
    
    # Could be elif here
    if len(ner_only) > 0:
        new_question = flag

        if ("the" in ner_only[0][0] 
            or "The" in ner_only[0][0]):
            new_question += ner_only[0][0] + " "
        else:
            new_question += "the " + ner_only[0][0] + " "

        for j in range(is_are_index+1, len(ner_tokens_sentence)):
            new_question += ner_tokens_sentence[j][0] + " "
    new_question = new_question[0:len(new_question)-1] # removes whitespace at end
    new_question += "?"


    return_list = [] # Is the return supposed to be a list? I guess multiple possible questions
    return_list.append(new_question)
    return return_list

a = generate_question("The Old Kingdom is most commonly regarded as the period from the Third Dynasty through to the Sixth Dynasty 2686–2181 BC")
print(a)
