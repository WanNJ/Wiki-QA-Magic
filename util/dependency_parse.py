"""
This file must have at least 2 different implementations for dependency parse.

Add implementations of coref resolution from different tools.
We need to compare the accuracy from the different tools and choose the best one.
We can do the testing manually by checking the output of different implementations.
"""

#from stanfordnlp.server import CoreNLPClient
#import os
from spacy.pipeline import DependencyParser

import spacy
nlp = spacy.load("en")


def get_dependency_parse_spacy(wiki_text_sent):
    """
    docstring here
        :param wiki_text_sent: 
    """
    #parser = DependencyParser(nlp.vocab)
    #doc = nlp("This is a sentence.")
    #processed = parser(doc)

    doc = nlp(wiki_text_sent)
    dependencies = []
    for token in doc:
        dependencies.append(token.dep_)
    return dependencies

def get_dependency_parse_corenlp(wiki_text_sent):
    """
    docstring here
        :param wiki_text_sent: 
    """

    """
    env = os.environ
    with CoreNLPClient(annotators=['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse', 'depparse', 'coref'],
                   timeout=80000, memory='16G') as client:
    ann = client.annotate(text)
    #sentence = ann.sentence[0]
    dependency_parse = sentence.basicDependencies
    return dependency_parse
    """
    pass

def get_dependency_parse_othertool(wiki_text_sent):
    """
    docstring here
        :param wiki_text_sent: 
    """
    pass