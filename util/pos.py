import spacy

nlp = spacy.load("en_core_web_lg")

def get_pos_spacy(text):
    doc = nlp(text)

    res = []
    for token in doc:
        res.append([token.text, token.pos_, token.tag_])

    return res

def get_pos_tokens_only_spacy(text):
    doc = nlp(text)

    res = []
    for token in doc:
        res.append(token.pos_)

    return res


