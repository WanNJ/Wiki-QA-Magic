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
        # print(ner_only)

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
            # 	quant_flag = True
            # 	quant_idx = idx
            # 	break

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

            # If all else fails to make a question, just replace the NE with "how many/how much"
            how_many_list = ["MONEY", "CARDINAL", "PERCENT", "QUANTITY"]
            ner_tags = util_service.get_ner_per_token(sentence)
            # new_tags = ner_tags
            # print(ner_tags)
            new_sent = ""
            added_q = False
            first_quote = True
            second_quote = False
            for idx, entry in enumerate(ner_tags):
            	if entry[1] in how_many_list:
            		if not added_q:
	            		if idx == 0:
	            			new_sent = new_sent + "How many" + " "
	            			added_q = True
	            		else:
	            			new_sent = new_sent + "how many" + " "
	            			added_q = True
            	elif entry[0] == ".":
            		new_sent = new_sent[0:len(new_sent)-1] + "?"
            	elif entry[0] == ",":
            		new_sent = new_sent[0:len(new_sent)-1] + ", "
            	elif entry[0] == '"':
            		if first_quote:
            			new_sent = new_sent + '"'
            			second_quote = True
            			first_quote = False
            		elif second_quote:
            			new_sent = new_sent[0:len(new_sent)-1] + '"' + " "
            			second_quote = False
            			first_quote = True
            	else:
            		new_sent = new_sent + entry[0] + " "
            return [new_sent]
        return []

    except:
        return []
    





# print(generate_question("It is the official language of China and Taiwan, as well as one of four official languages of Singapore."))

# print(generate_question("It is one of the six official languages of the United Nations."))

# print(generate_question("In his rookie season, he started 23 of 24 matches scoring seven goals."))

# print(generate_question("Two weeks later, he opened the scoring in Fulham's 1–1 away draw against Wigan Athletic."))

# print(generate_question("On August 31, 2012, Dempsey joined Tottenham Hotspur on a three-year contract for a fee believed to be in the region of $9 million."))

# print(generate_question("On August 3, 2013, Dempsey signed with MLS club Seattle Sounders FC as a Designated Player on a four-year contract, for a transfer fee of $9 million."))

# print(generate_question("One unusual feature of Barnard 68 is its vibrations, which have a period of 250,000 years."))

# print(generate_question("The optical companion is of magnitude 8.2."))

# print(generate_question('Evan eats "around" 12 pounds of food a day.'))
