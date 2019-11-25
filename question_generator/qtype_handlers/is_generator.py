import sys
sys.path.append("../..")
import util_service
from . get_is_are_was_were_loc import which_acomp


def build_sides(ner_tags, is_are_index):
    first_half = ""
    second_half = ""
    # print(ner_tags)
    # print(is_are_index)
    punct = [".", "?", "!", ","]
    for i in range(is_are_index):
        if ner_tags[i][0] not in punct:
            first_half += ner_tags[i][0] + " "
        else:
            first_half = first_half[0:len(first_half) - 1] + ner_tags[i][0] + " "

    for j in range(is_are_index + 1, len(ner_tags)):
        if ner_tags[j][0] not in punct:
            second_half += ner_tags[j][0] + " "
        else:
            second_half = second_half[0:len(second_half) - 1] + ner_tags[j][0] + " "

    # print(first_half)
    # print(second_half)
    second_half = second_half[0:len(second_half)-1]
    first_letter = first_half[0:1].lower()
    first_half = first_letter + first_half[1:len(first_half)]
    return first_half, second_half


def generate_question(sentence):
    """
    Takes in a string sentence and generates a "Is" question.
    Puts "Is the " + named entity + rest_of_sentence + "?"
    """

    ner_tags = util_service.get_ner_per_token(sentence)
    # ner_only = util_service.get_ner(sentence)

    # # No questions to be made without any named entities
    # if len(ner_only) == 0:
    #     return []

    # # Right now instead of this block it just adds "the " in the question later
    # # This block would add "the " to the named entity if "the" is 
    # # in the sentence right before where the named entity is
    # ner_start = ner_only[0][1]
    # list_of_the = ["The", "the"]
    # # sentence[ner_start - 4:ner_start] looks for "the"
    # if sentence[ner_start - 4 : ner_start-1] in list_of_the:
    #     ner_only[0][0] = "the " + ner_only[0][0]
        

    # print(ner_only)
    # print(ner_tokens_sentence)

    

    # Finds where the is word is, then is just going to append everything after it 
    # into a question
    is_are_index = -1
    # is_was_are_were is a string (one of "Is ", "Are ", "Was ", or "Were ")
    # is_are_index is where this string occurs in the tokens
    # is_was_are_were, is_are_index = which_acomp(ner_tokens_sentence)

    is_was_are_were, is_are_index = which_acomp(ner_tags)
    before_sentence_2, after_sentence_2 = build_sides(ner_tags, is_are_index)
    sentence_2 = is_was_are_were + before_sentence_2 + after_sentence_2
    
    # # Could be elif here
    # if len(ner_only) > 0:
    #     new_question = is_was_are_were

    #     new_question += ner_only[0][0] + " "

        # if ("the" in ner_only[0][0] 
        #     or "The" in ner_only[0][0]):
        #     new_question += ner_only[0][0] + " "
        # else:
        #     new_question += ner_only[0][0] + " "

    #     for j in range(is_are_index+1, len(ner_tokens_sentence) -1): #up to -1 as the last token is "."
    #         new_question += ner_tokens_sentence[j][0] + " "
    # new_question = new_question[0:len(new_question)-1] # removes whitespace at end
    # new_question += "?"


    # return_list = [] # Is the return supposed to be a list? I guess multiple possible questions
    # return_list.append(new_question)
    sentence_2 = sentence_2[0:len(sentence_2)-1] + "?"
    return [sentence_2]


# a = generate_question("The Old Kingdom is most commonly regarded as the period from the Third Dynasty through to the Sixth Dynasty 2686–2181 BC.")
# print(a)

# b = generate_question("Andrés Iniesta Luján (Spanish pronunciation: [anˈdɾes iˈnjesta luˈxan]; born 11 May 1984) is a Spanish professional footballer who plays as a central midfielder for FC Barcelona and the Spain national team.")
# print(b)


# ['Is The Old Kingdom most commonly regarded as the period from the Third Dynasty through to the Sixth Dynasty 2686–2181 BC?']
# ['Is Andrés Iniesta Luján a Spanish professional footballer who plays as a central midfielder for FC Barcelona and the Spain national team?']





