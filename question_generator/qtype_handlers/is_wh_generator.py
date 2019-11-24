import re
import util_service
import sys
sys.path.append("../..")


def get_is_idx_from_ner(ner_tags):
    for idx, entry in enumerate(ner_tags):
        if entry[0].lower() == "is":
            return idx
    return -1


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

    is_idx = 0

    sent_tokens = sentence.split()

    # get index of is
    try:
        is_idx = sent_tokens.index("is")
    except:
        return []

    # getting the end of question
    passed_tokens = []
    for i, token in enumerate(sent_tokens):
        if i >= is_idx:
            if (i == is_idx+1):
                if token in ["of"]:
                    continue
            passed_tokens.append(token)

    # replaces . with ? if it is last token or it is a part of last token
    if passed_tokens[-1] == ".":
        passed_tokens[-1] = "?"
    elif passed_tokens[-1].endswith("."):
        passed_tokens[-1] = re.sub("(.*)\.", "\\1?", passed_tokens[-1])
    else:
        passed_tokens.append("?")

    # need to identify q_type
    # could be who, what
    # from NER
    # if it is GPE then "what"
    # if it is "PERSON" or "PRON" then "who"
    # dep parse is not providing expected output Old Kingdom is coming as pnoun
    q_type = ""

    # dep_parse = util_service.get_dep_parse_tree(sentence)[1]
    pos_tags = util_service.get_pos(sentence)
    ner_tags = util_service.get_ner_per_token(sentence)
    is_idx_ner = get_is_idx_from_ner(ner_tags)
    if is_idx_ner != -1:
        if ner_tags[is_idx_ner - 1][1] == "GPE":
            q_type = "What"
        elif ner_tags[is_idx_ner - 1][1] == "PERSON":
            q_type = "Who"
        elif ner_tags[is_idx_ner - 1][0] == "," and ner_tags[is_idx_ner - 2][1] == "PERSON":
            q_type = "Who"
        # checks if there is a pronoun before is word from pos tags
        elif pos_tags[is_idx - 1][1] == "PRON":
            q_type = "Who"
    if q_type == "":
        return []

    q = q_type + " " + " ".join(passed_tokens)
    return [q]
