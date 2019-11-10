"""
This file must have at least 2 implementations for NER
"""

import spacy
nlp = spacy.load("en")#("en_core_web_lg")

def get_ner_spacy(text):
    """
    gets the named entities in a string of text 
        :param text: string of a wikipedia article (or sentence)
    """

    named_entities = []
    doc = nlp(text)

    for ent in doc.ents:
    	named_entities.append([ent.text, ent.start_char, ent.end_char, ent.label_])
    	
    return named_entities

def get_ner_per_token_spacy(text):
    """
    gets the named entities in a string of text per token
        :param text: string of a wikipedia article (or sentence)
    """

    token_named_entities = []
    doc = nlp(text)

    for token in doc:
        token_named_entities.append([token.text, token.ent_type_])
    return token_named_entities

if __name__ == "__main__":
    print(get_ner_per_token_spacy("Pittsburgh is located in Pennsylvania."))
