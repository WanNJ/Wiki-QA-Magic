import re
import sys
sys.path.append("../..")
import util_service

from question_generator.qtype_handlers.get_is_are_was_were_loc import which_acomp

# def find_about_money(sentence):
#   if (   sentence.find("value") != -1
#       or sentence.find("worth") != -1
#       or sentence.find("$") != -1
#       or sentence.find("£") != -1
#       or sentence.find("€") != -1):
#       return True
#   return False

def get_possible_entity(ner_only):
    impossible_tags = ["DATE", "MONEY", "LAW", "LANGUAGE", "PERCENT", "TIME"]

    for idx, entry in enumerate(ner_only):
        if entry[3] not in impossible_tags:
            return entry[0]
    return "" 



def generate_question(sentence):

    # passed_tokens = []
 #    for i, token in enumerate(sent_tokens):
 #        if i >= is_idx:
 #            if (i == is_idx+1):
 #                if token in ["of"]:
 #                    continue
 #            passed_tokens.append(token)

 #    # replaces . with ? if it is last token or it is a part of last token
 #    if passed_tokens[-1] == ".":
 #        passed_tokens[-1] = "?"
 #    elif passed_tokens[-1].endswith("."):
 #        passed_tokens[-1] = re.sub("(.*)\.", "\\1?", passed_tokens[-1])
 #    else:
 #        passed_tokens.append("?")

    try:
        ner_only = util_service.get_ner(sentence)

        sent_tokens = sentence.split()

        is_was_are_were = ""
        try:
            is_was_are_were, is_are_index = which_acomp(ner_tags)
        except:
            pass

        money_flag = False
        for idx, entry in enumerate(ner_only):
            if entry[3] == "MONEY":
                money_flag = True
                money_idx = idx
                break
            # elif entry[3] == "QUANTITY":

            # elif entry[3] == "CARDINAL":
            # elif entry[3] == "PERCENT":


        if len(ner_only) > 1:
            if money_flag:
                other_named_entity = get_possible_entity(ner_only)
                
                # if ner_only[0][3] not in impossible_tags:
                #      other_named_entity = ner_only[0][0]
                if is_was_are_were != "" and other_named_entity != "":
                    q = "How much " + is_was_are_were + other_named_entity + " " + "worth?"
                elif other_named_entity != "":
                    q = "How much did " + other_named_entity + " " + "cost?"
                else:
                    return []
                return [q]

    except:
        return []
    





# generate_question("It is the official language of China and Taiwan, as well as one of four official languages of Singapore.")

# generate_question("It is one of the six official languages of the United Nations.")

# generate_question("In his rookie season, he started 23 of 24 matches scoring seven goals.")

# generate_question("Two weeks later, he opened the scoring in Fulham's 1–1 away draw against Wigan Athletic.")

# print(generate_question("On August 31, 2012, Dempsey joined Tottenham Hotspur on a three-year contract for a fee believed to be in the region of $9 million."))

# print(generate_question("On August 3, 2013, Dempsey signed with MLS club Seattle Sounders FC as a Designated Player on a four-year contract, for a transfer fee of $9 million."))




