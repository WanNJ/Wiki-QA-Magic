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


def get_dependency_parse_spacy(text):
    """
    docstring here
        :param text: 
    """
    doc = nlp(text)
    dependencies = []
    for token in doc:
        dependencies.append(token.dep_)
    return dependencies

def get_dependency_parse_corenlp(text):
    """
    docstring here
        :param text: 
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

def get_dependency_parse_othertool(text):
    """
    docstring here
        :param wiki_text_sent: 
    """
    pass