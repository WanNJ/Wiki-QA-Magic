import sys
sys.path.append("../..")
import util_service

from question_generator.qtype_handlers.get_is_are_was_were_loc import which_acomp


def get_diff_date(date):
    # July 2, 1989
    # 1989
    year = date[len(date)-4:len(date)]
    year = int(year) + 4
    return str(year)

def get_is_idx_from_ner(ner_tags):
    for idx, entry in enumerate(ner_tags):
        if entry[0].lower() == "is":
            return idx
    return -1

def get_was_idx_from_ner(ner_tags):
    for idx, entry in enumerate(ner_tags):
        if entry[0].lower() == "was":
            return idx
    return -1


def generate_question(sentence):
    try:
        is_idx = -1
        was_idx = -1

        sent_tokens = sentence.split()

        # get index of is
        try:
            is_idx = sent_tokens.index("is")
            was_idx = sent_tokens.index("was")
        except: pass

        # getting the end of question
        if is_idx != -1:
            passed_tokens = []
            for i, token in enumerate(sent_tokens):
                if i > is_idx:
                    if (i == is_idx+1):
                        if token in ["of"]:
                            continue
                    passed_tokens.append(token)
                    
        elif was_idx != -1:
            passed_tokens = []
            for i, token in enumerate(sent_tokens):
                if i > was_idx:
                    if (i == was_idx+1):
                        if token in ["of"]:
                            continue
                    passed_tokens.append(token)

        ner_tags = util_service.get_ner_per_token(sentence)
        is_idx_ner = get_is_idx_from_ner(ner_tags)
        was_idx_ner = get_was_idx_from_ner(ner_tags)
        acomp_idx_ner = max(is_idx_ner, was_idx_ner)
        if acomp_idx_ner != -1:
            if (ner_tags[acomp_idx_ner - 1][1] == "ORG"
                or ner_tags[acomp_idx_ner - 1][1] == "GPE"):
                # q_type = "What"
                wrong = "Apple Inc."
            elif ner_tags[acomp_idx_ner - 1][1] == "PERSON":
                # q_type = "Who"
                wrong = "Bill Nye"
            elif ner_tags[acomp_idx_ner - 1][1] == "DATE":
                wrong = get_diff_date(ner_tags[acomp_idx_ner - 1][0])
            elif ner_tags[acomp_idx_ner - 1][1] == "LOC":
                # q_type = "Who"
                wrong = "America"
            elif ner_tags[acomp_idx_ner - 1][1] == "QUANTITY":
                # q_type = "Who"
                wrong = "42"
            elif ner_tags[acomp_idx_ner - 1][1] == "MONEY":
                # q_type = "Who"
                wrong = "$42"
            elif ner_tags[acomp_idx_ner - 1][1] == "PERCENT":
                # q_type = "Who"
                wrong = "42%"
        # q = "Is " + ner_tags[acomp_idx_ner - 1][0] + " " + " ".join(passed_tokens) + " or " + wrong + "?"
        ner_only = util_service.get_ner(sentence)
        print(ner_only)
        q = "Is " + ner_only[0][0] + " " + " ".join(passed_tokens) + " or " + wrong + "?"
        print(q)
        return [q]
    except:
        return []

# sentence = "Old Kingdom is most commonly regarded as the period from the Third Dynasty through to the Sixth Dynasty ."
# sentence = "King Djoser's architect, Imhotep is credited with the development of building with stone and with the conception of the new architectural form—the Step Pyramid."
# sentence = "The Old Kingdom is perhaps best known for the large number of pyramids constructed at this time as burial places for Egypt's kings."
# sentence = 'For this reason, the Old Kingdom is frequently referred to as "the Age of the Pyramids."'
# sentence = "The first is called the Meidum pyramid, named for its location in Egypt."
# sentence = "There were military expeditions into Canaan and Nubia, with Egyptian influence reaching up the Nile into what is today the Sudan."
# sentence = "She is a forward for the Orlando Pride and the United States women's national soccer team."
# sentence = """Alexandra "Alex" Patricia Morgan Carrasco (born July 2, 1989), née Alexandra Patricia Morgan, is an American soccer player, Olympic gold medalist, and FIFA Women's World Cup champion."""

# generate_question("Alex Jones buyout clause is valued at €1 billion.")
# generate_question("""Alexandra "Alex" Patricia Morgan Carrasco (born July 2, 1989), née Alexandra Patricia Morgan, is an American soccer player, Olympic gold medalist, and FIFA Women's World Cup champion.""")
# generate_question("Alex Jones is a forward for the Orlando Pride and the United States women's national soccer team.")
# generate_question('For this reason, the Old Kingdom is frequently referred to as "the Age of the Pyramids."')
# generate_question("A member of the inaugural class of the U.S. Soccer residency program in Bradenton, Florida, Donovan was declared player of the tournament for his role in the United States U17 squad that finished fourth in the 1999 FIFA U-17 World Championship.")
# generate_question("In Major League Soccer, Donovan won a record six MLS Cups and is both the league's all-time top scorer with 144 goals and the league's all-time assists leader with 136.")
# generate_question("Donovan was born on March 4, 1982, in Ontario, California, to Donna Kenney-Cash, a special education teacher, and Tim Donovan, a semi-professional ice hockey player originally from Canada, which makes Donovan a Canadian citizen by descent. His mother raised him and his siblings in Redlands, California.")
# generate_question("The Galaxy had another successful campaign in 2010 winning the Supporters' Shield for the first time since 2003.")
# generate_question("Donovan married actress Bianca Kajlich on December 31, 2006; the couple separated in July 2009, and Donovan filed for divorce in December 2010.")
# # generate_question("In 1997, Alex Jones moved to Sporting CP.")
# # generate_question("In 2003 Alex Jones signed for Manchester United for £12.2 million (€15 million).")
# generate_question("His buyout clause is valued at €1 billion.")







