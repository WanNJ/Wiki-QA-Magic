"""
This file must have at least 2 implementations for NER
"""

#from stanfordnlp.server import CoreNLPClient
#import os

from spacy.pipeline import EntityRecognizer

from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
nlp = English()

import spacy
nlp = spacy.load("en") # en_core_web_sm

def get_ner(wiki_text):
    """
    gets the named entities in a string of text 
        :param wiki_text: string of a wikipedia article (or sentence)
    """

    named_entities = []
    doc = nlp(wiki_text)
    #print(doc)
    #print(doc.ents)
    for ent in doc.ents: #where ent is entity
    	named_entities.append([ent.text, ent.start_char, ent.end_char, ent.label_])
    	#print(ent.text, ent.start_char, ent.end_char, ent.label_)

    #ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    #print("ENTS", ents)
    
    return named_entities
    #ner = EntityRecognizer(nlp.vocab)





#get_ner("This is an article about Evan. He is 22, halfway to 23. This is to test if the program spacy will correctly found out that he refers to Evan.")
