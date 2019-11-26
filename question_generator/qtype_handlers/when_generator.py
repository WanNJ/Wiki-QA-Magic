import re
import sys
sys.path.append("../..")
import util_service


#def get_questions_from_pattern1()

def generate_question(sentence):
    # print("-=-==-=-")
    # print(sentence)
    # print("-=-==-=-")
    
    ## pattern 1
    # sentence = "In January 2012, Morgan and national teammate Heather Mitts became brand ambassadors for health product company, GNC."
    # sentence = "In July 2011, Morgan signed a one-year endorsement deal with Bank of America."
    # sentence = "In 2013, Morgan appeared in television commercials for Bridgestone."
    # sentence = "In 2015, Morgan starred in a Nationwide Mutual Insurance Company commercial that that was broadcast nationwide in the United States."
    # sentence = "In May 2015, Morgan was featured on the cover of ESPN The Magazine with teammates Abby Wambach and Sydney Leroux."
    # sentence = "In 2013, Morgan appeared in the ESPN documentary series, Nine for IX."
    # sentence = "In May of the same year, Morgan likeness appeared on The Simpsons along with Christen Press and Abby Wambach."
    # sentence = "On August 31, 2013, Portland captured the inaugural National Women’s Soccer League championship title after defeating regular season champions Western New York Flash 2–0."
    # sentence = "Throughout the 2011 season, Morgan played in 14 matches and scored 4 goals."
    # sentence = "At age 17, Morgan was called up to the United States"
    # sentence = "In the 2012 London Olympics She scored the game-winning goal in the 123rd minute of the semifinal game against Canada."

    # TODO:
    # ## pattern 2 to be built later
    # sentence = "Morgan married Servando Carrasco, also a soccer player, on December 31, 2014."
    
    util_service.get_dep_parse_tree(sentence)[1]
    pos_tags = util_service.get_pos(sentence)
    ner_tags = util_service.get_ner_per_token(sentence)

    sent_tokens = util_service.get_tokenized_form(sentence)
    
    lemma_tokens = util_service.get_lemmatize_form(sentence)

    ## in {date}, Nsub Verb
    ## look for the above pattern only, if result found return
    ## other patterns to be identified and invoked later
    
    date_span = []
    for i, sent_token in enumerate(sent_tokens):
        if i==0 and sent_tokens[i].lower() in ["in", "on", "throughout", "at"]:
            date_span.append(i)
            continue
        if ner_tags[i][1] == "DATE":
            date_span.append(i)
            continue
        if sent_tokens[i] == ",":
            date_span.append(i)
            continue
        break
    
    if not len(date_span):
        return []

    question_sent = []
    first_verb_flag = False
    if pos_tags[date_span[-1]+1][1] in ["PROPN"]:
        for i, sent_token in enumerate(sent_tokens):
            if i <= date_span[-1]:
                continue
            # convert only 1st verb to lemma
            # overfitting for sentences consiting two verbs, eg second verb defeating, would change to defeat -> On August 31, 2013, Portland captured the inaugural National Women’s Soccer League championship title after defeating regular season champions Western New York Flash 2–0.
            if pos_tags[i][1] == "VERB" and not first_verb_flag:
                if sent_token != "was": # check for passive voice
                    question_sent.append(lemma_tokens[i])
                    first_verb_flag = True
                    continue
                continue
            if sent_token == "\n":
                continue
            question_sent.append(sent_token)
    
    if not len(question_sent):
        return []

    # replaces . with ? if it is last token or it is a part of last token
    if question_sent[-1] == ".":
        question_sent[-1] = "?"
    elif question_sent[-1].endswith("."):
        question_sent[-1] = re.sub("(.*)\.", "\\1?", question_sent[-1])
    else:
        question_sent.append("?")

    
    q_when = "When did " + " ".join(question_sent)
    q_did = "Did " + " ".join(question_sent)


    return [q_when, q_did]



# Could be a WHEN question
# a = generate_question("The Old Kingdom is most commonly regarded as the period from the Third Dynasty through to the Sixth Dynasty 2686–2181 BC")
