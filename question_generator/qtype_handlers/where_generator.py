import re
import sys
sys.path.append("../..")
import util_service

from question_generator.qtype_handlers.get_is_are_was_were_loc import which_acomp


def get_is_idx_from_ner(ner_tags):
    for idx, entry in enumerate(ner_tags):
        if entry[0].lower() == "is":
            return idx
    return -1

def get_in_idx_from_ner(ner_tags):
    for idx, entry in enumerate(ner_tags):
        if entry[0].lower() == "in":
            return idx
    return -1

def get_was_idx_from_ner(ner_tags):
    for idx, entry in enumerate(ner_tags):
        if entry[0].lower() == "was":
            return idx
    return -1


def get_location(ner_tags, in_idx, ner_only):
    """
    Given that "in" is in the sentence, it builds the location
    for the birthday stuff
    """
    try:
        location = ""
        index = 0
        if in_idx != -1:
            index = in_idx + 1
            while (index < len(ner_tags) and (
                ner_tags[index][1] == "ORG"
                or ner_tags[index][1] == "GPE"
                or ner_tags[index][1] == "LOC"
                or ner_tags[index][1] == "PERSON"
                or ner_tags[index][0] == ",")):
                if ner_tags[index][0] == ",":
                    location += ner_tags[index][0]
                    index += 1
                else:
                    location += " " + ner_tags[index][0] 
                    index += 1
        else:
            for idx, named_entity in enumerate(ner_only):
                if (named_entity[idx][3] == "ORG"
                or named_entity[idx][3] == "GPE"
                or named_entity[idx][3] == "LOC"):
                    return named_entity[idx][3]

        if location[len(location)-2] == ",":
            location = location[1:len(location)-2]
        else:
            location = location[1:len(location)-1]

    except:
        return ""

    return location


def build_sides(ner_tags, is_are_index):
    """
    This is for the below transition:
    # "Some sets for the film were built in Glen Coe, Scotland, near the Clachaig Inn." # sentence 1
    # "Were some sets for the film built in Glen Coe, Scotland, near the Clachaig Inn?" # sentence 2,
    so basically has the is_are_were_was position and gets all the stuff on both sides
    """
    try:
        first_half = ""
        second_half = ""
        # print(is_are_in
        # print(ner_tags)dex)
        punct = [".", "?", "!", ",", "'"]
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
    except: return "", ""

    return first_half, second_half

def change_2_to_4(sentence_2, last_named_entity):
    """
    Does the following example:
    # "Were some sets for the film built in Glen Coe, Scotland, near the Clachaig Inn?" # sentence 2
    # "Were some sets for the film built in Glen Coe, Scotland, near where?" # sentence 3
    # "Where were some sets for the film built in Glen Coe, Scotland, near?" # sentence 4

    Finds the last named entity, sees if it's a "where" thing, then 
    uses "What" or "Where" in place at the front, otherwise
    returns False and makes the overall generate_question function return []
    """
    try:
        named_entity = last_named_entity[0]
        entity_index = sentence_2.find(named_entity)
        places = ["LOC", "GPE"]
        things = ["ORG"]
        if last_named_entity[3] in places:
            q_type = "Where"
            q_flag = True
        elif last_named_entity[3] in things:
            q_type = "What"
            q_flag = True
        else:
            return "", False
        # sentence_3 = sentence_2[0:entity_index] + q_type
        sentence_3 = sentence_2[0:entity_index] # not technically 3 but w/e
        first_letter = sentence_3[0:1].lower()
        sentence_3 = first_letter + sentence_3[1:len(sentence_3) - 1]
        sentence_4 = q_type + " " + sentence_3 + "?"
        sent_4_len = len(sentence_4)
        of_in = [" of?", " in?"]
        if sentence_4[sent_4_len-4:sent_4_len] in of_in:
            sentence_4 = sentence_4[0:sent_4_len-4] + "?"
    except:
        return "", False
    return sentence_4, q_flag






    
# A lot of the stuff here is extraneous but the important parts are commented
def generate_question(sentence):
    """
    generates what question based on the sentence
        :param sentence: 

    
    """
    # sentence = "Old Kingdom is most commonly regarded as the period from the Third Dynasty through to the Sixth Dynasty ."
    # sentence = "King Djoser's architect, Imhotep is credited with the development of building with stone and with the conception of the new architectural form—the Step Pyramid."
    # sentence = "The Old Kingdom is perhaps best known for the large number of pyramids constructed at this time as burial places for Egypt's kings."
    # sentence = 'For this reason, the Old Kingdom is frequently referred to as "the Age of the Pyramids."'
    # sentence = "The first is called the Meidum pyramid, named for its location in Egypt."
    # sentence = "There were military expeditions into Canaan and Nubia, with Egyptian influence reaching up the Nile into what is today the Sudan."
    # sentence = "She is a forward for the Orlando Pride and the United States women's national soccer team."
    # sentence = """Alexandra "Alex" Patricia Morgan Carrasco (born July 2, 1989), née Alexandra Patricia Morgan, is an American soccer player, Olympic gold medalist, and FIFA Women's World Cup champion."""

    # sentence = "List of Olympic medalists in football"
    # util_service.get_dep_parse_tree(sentence)[1]
    # util_service.get_pos(sentence)

    is_idx = -1
    was_idx = -1
    born_idx = -1
    in_idx = -1

    sent_tokens = sentence.split()

    # get index of is
    try: is_idx = sent_tokens.index("is")
    except: pass

    try: born_idx = sent_tokens.index("born")
    except: pass

    try: was_idx = sent_tokens.index("was")
    except: pass

    try: in_idx = sent_tokens.index("in")
    except: pass

    ner_only = util_service.get_ner(sentence)
    # print(ner_only)
    ner_tags = util_service.get_ner_per_token(sentence)
    # print(ner_tags)
    # dep_parse = util_service.get_dep_parse_tree_Evan(sentence) #heads children
    # print(dep_parse)

    was_idx_ner = -1
    is_idx_ner = -1

    if was_idx != -1:
        was_idx_ner = get_was_idx_from_ner(ner_tags)
    if is_idx != -1:
        is_idx_ner = get_is_idx_from_ner(ner_tags)
    if in_idx != -1:
        in_idx_ner = get_in_idx_from_ner(ner_tags)

    # This is specific to where someone was born (rather, who was born in _location_)
    idx_ner = max(was_idx_ner, is_idx_ner)
    if (ner_tags[idx_ner - 1][1] == "PERSON"):
        if born_idx != -1:
            location = get_location(ner_tags, in_idx_ner, ner_only)
            # print("Loc: ", location)
            q = "Who was born in " + location + "?"
            # print([q])
            return [q]
        else: 
            q_type = ""

    # This tries to flip the end to the beginning, see following example:
    # "Some sets for the film were built in Glen Coe, Scotland, near the Clachaig Inn." # sentence 1
    # "Were some sets for the film built in Glen Coe, Scotland, near the Clachaig Inn?" # sentence 2
    # "Were some sets for the film built in Glen Coe, Scotland, near where?" # sentence 3
    # "Where were some sets for the film built in Glen Coe, Scotland, near?" # sentence 4

    try:
        is_was_are_were, is_are_index = which_acomp(ner_tags)
        before_sentence_2, after_sentence_2 = build_sides(ner_tags, is_are_index)
        sentence_2 = is_was_are_were + before_sentence_2 + after_sentence_2
        # print(sentence_2)
        last_named_entity = ner_only[len(ner_only) - 1]
        sentence_4, ended_with_where_or_what = change_2_to_4(sentence_2, last_named_entity)
        if not ended_with_where_or_what:
            return []
        return [sentence_4]
    # sentence_4 = change_2_to_4(sentence_3)
    # print(sentence_4)
    except:
        return []
    return []
    





generate_question("Some sets for the film were built in Glen Coe, Scotland, near the Clachaig Inn.")

a = generate_question("Lionel Andrés Messi was born on 24 June 1987 in Rosario, Santa Fe, the third of four children of Jorge Messi, a steel factory manager, and his wife Celia Cuccittini, who worked in a magnet manufacturing workshop.")
# print(a)

b = generate_question("The first is called the Meidum pyramid, named for its location in Egypt.")
# print(b)

generate_question("In Covent Garden one evening, he boasts to a new acquaintance, Colonel Hugh Pickering (Wilfrid Hyde-White), himself an expert in phonetics, that he could teach any person to speak in a way that he could pass them off as a duke or duchess at an embassy ball.")
# ("Harry Potter, now aged 13, has been spending another dissatisfying summer at Privet Drive.")
generate_question("Growing up in Nacogdoches, Texas, Dempsey played for one of the top youth soccer clubs in the state, the Dallas Texans, before playing for Furman University's men's soccer team.")
# ("The trio are returning to Hogwarts for the school year on the Hogwarts Express when dementors suddenly board the train, searching for Sirius.")

generate_question("Donovan was born on March 4, 1982, in Ontario, California, to Donna Kenney-Cash, a special education teacher, and Tim Donovan, a semi-professional ice hockey player originally from Canada, which makes Donovan a Canadian citizen by descent.")
# generate_question("The brightest star in Gemini is Pollux, and the second brightest is Castor.") #[['Gemini', 22, 28, 'ORG'], ['Pollux', 32, 38, 'GPE'], ['second', 48, 54, 'ORDINAL']]
# generate_question("Python was conceived in the late 1980s, and its implementation was started in December 1989 by Guido van Rossum at CWI in the Netherlands as a successor to the ABC language (itself inspired by SETL) capable of exception handling and interfacing with the Amoeba operating system.")

generate_question("Python 2.0 was released on 16 October 2000 and had many major new features, including a cycle-detecting garbage collector and support for Unicode.")

generate_question("It was envisioned that Hindi would become the sole working language of the Union Government by 1965 (per directives in Article 344 (2) and Article 351), with state governments being free to function in the language of their own choice.")

generate_question("Urdu is the official language of Pakistan, and is one of the 22 official languages of India.")

generate_question("It is the official language of China and Taiwan, as well as one of four official languages of Singapore.")

generate_question("English is one of the six official languages of the United Nations.")

generate_question("In his rookie season, he started 23 of 24 matches scoring seven goals.")

generate_question("Two weeks later, he opened the scoring in Fulham's 1–1 away draw against Wigan Athletic.")

generate_question("On August 31, 2012, Dempsey joined Tottenham Hotspur on a three-year contract for a fee believed to be in the region of $9 million.")

generate_question("On August 3, 2013, Dempsey signed with MLS club Seattle Sounders FC as a Designated Player on a four-year contract, for a transfer fee of $9 million.")

generate_question("The language was initially called Oak after an oak tree that stood outside Gosling's office.")

generate_question("Dempsey was born in Nacogdoches, Texas, and, for much of his childhood, his family lived in a trailer park, where he and his siblings grew up playing soccer with Hispanic immigrants.")

generate_question("He attended Furman University as a health and exercise science major and a key player for Paladins soccer.")

generate_question("He scored the game-winning goal in the Eastern Conference Final on his way to an appearance in the MLS Cup Final.")

generate_question("Before moving to Fulham, Dempsey went for a trial at ŁKS Łomża where the coach sent him to Fulham.")

generate_question("On September 18, 2010, he scored an equalizing goal on 56 minutes with a header against Blackburn Rovers at Ewood Park in the 1–1 draw to continue Fulham's unbeaten record in the Barclays Premier League.")

generate_question("In the FA Cup 3rd round he scored a double against Coventry City.")

# "It is one of the six official languages of the United Nations."
# "Is it one of the six official languages of the United Nations."
# "Is it one of the six official languages of what."
# "What is one of the six official languages of ."



# "The first is called the Meidum pyramid, named for its location in Egypt."
# "Is the first called the Meidum pyramid, named for its location in where."
# "Where is the first called the Meidum pyramid, named for its location."





