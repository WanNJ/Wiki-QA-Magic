"""
This file must have at least 2 different implementations for dependency parse.

Add implementations of coref resolution from different tools.
We need to compare the accuracy from the different tools and choose the best one.
We can do the testing manually by checking the output of different implementations.
"""

# from stanfordnlp.server import CoreNLPClient
# import os
from spacy.pipeline import DependencyParser
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_lg")

def get_dep_parse_tree_spacy(text):
    """
    Return the noun-chunks and dependency parse tree
    :param text:
    :return: the doc, chunks and dep-parse-tree
    """
    doc = nlp(text)
    # Uncomment the following line and render the result as html to visualize the dependency diagram
    # print(displacy.render(doc, style='dep'))
    res = []
    for token in doc:
        res.append([token.text, token.i, token.dep_, token.head, [child.i for child in token.children]])

    return doc, res

def get_dependency_parse_spacy(text):
    """
    Returns the dependency parse tags of each token in the text.
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
